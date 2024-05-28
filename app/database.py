import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="pokedex"
)

def get_pokemon(pokemon_id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemon WHERE id = %s", (pokemon_id,))
    pokemon = cursor.fetchone()
    cursor.close()
    return pokemon

def get_pokemon_by_id(pokemon_id):
    pokemon = get_pokemon(pokemon_id)
    if pokemon:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT type FROM pokemon_type WHERE pokemon_id = %s", (pokemon_id,))
        types = [row['type'] for row in cursor.fetchall()]
        cursor.execute("SELECT ability FROM pokemon_ability WHERE pokemon_id = %s", (pokemon_id,))
        abilities = [row['ability'] for row in cursor.fetchall()]
        cursor.close()
        pokemon['types'] = types
        pokemon['abilities'] = abilities
    return pokemon

def create_pokemon(pokemon_data):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pokemon 
        (id, name, hp, attack, defense, sp_attack, sp_defense, speed, image_url) 
        VALUES 
        (%(id)s, %(name)s, %(hp)s, %(attack)s, %(defense)s, %(sp_attack)s, %(sp_defense)s, %(speed)s, %(image_url)s)
    """, pokemon_data)
    conn.commit()
    cursor.close()
    return {"message": "Nouveau Pokemon avec succes"}

def update_pokemon(pokemon_id, pokemon_data):
    cursor = conn.cursor()
    set_clause = ", ".join([f"{key} = %({key})s" for key in pokemon_data.keys()])
    pokemon_data["pokemon_id"] = pokemon_id
    cursor.execute(f"""
        UPDATE pokemon
        SET {set_clause}
        WHERE id = %(pokemon_id)s
    """, pokemon_data)
    conn.commit()
    cursor.close()
    return {"message": "Pokemon mise a jour success"}

def delete_pokemon(pokemon_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pokemon_type WHERE pokemon_id = %s", (pokemon_id,))
    cursor.execute("DELETE FROM pokemon_ability WHERE pokemon_id = %s", (pokemon_id,))
    cursor.execute("DELETE FROM pokemon WHERE id = %s", (pokemon_id,))
    conn.commit()
    cursor.close()
    return {"message": "Pokemon supprimer success"}

def get_all_pokemons(skip: int = 0, limit: int = 10):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemon LIMIT %s OFFSET %s", (limit, skip))
    pokemons = cursor.fetchall()
    cursor.close()
    return pokemons

def add_pokemon_type(pokemon_id, type):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon_type (pokemon_id, type) VALUES (%s, %s)", (pokemon_id, type))
    conn.commit()
    cursor.close()
    return {"message": "Type ajouter success"}

def add_pokemon_ability(pokemon_id, ability):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon_ability (pokemon_id, ability) VALUES (%s, %s)", (pokemon_id, ability))
    conn.commit()
    cursor.close()
    return {"message": "Capaciter ajouter success"}

def delete_pokemon_type(pokemon_id, type):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pokemon_type WHERE pokemon_id = %s AND type = %s", (pokemon_id, type))
    conn.commit()
    cursor.close()
    return {"message": "Type supprimer success"}

def delete_pokemon_ability(pokemon_id, ability):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pokemon_ability WHERE pokemon_id = %s AND ability = %s", (pokemon_id, ability))
    conn.commit()
    cursor.close()
    return {"message": "Competence supprimer success"}


