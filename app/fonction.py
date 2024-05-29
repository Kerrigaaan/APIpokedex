from .database import conn

# Obtient un Pokémon en fonction de son identifiant.
def get_pokemon(pokemon_id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemon WHERE id = %s", (pokemon_id,))
    pokemon = cursor.fetchone()
    cursor.close()
    return pokemon

# Obtient un Pokémon et ses types et capacités associés en fonction de son identifiant.
def get_pokemon_by_id(pokemon_id):
    pokemon = get_pokemon(pokemon_id)
    if pokemon:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT t.type FROM pokemon_type pt JOIN type t ON pt.type_id = t.id WHERE pt.pokemon_id = %s", (pokemon_id,))
        types = [row['type'] for row in cursor.fetchall()]
        cursor.execute("SELECT a.ability FROM pokemon_ability pa JOIN ability a ON pa.ability_id = a.id WHERE pa.pokemon_id = %s", (pokemon_id,))
        abilities = [row['ability'] for row in cursor.fetchall()]
        cursor.close()
        pokemon['types'] = types
        pokemon['abilities'] = abilities
    return pokemon

# Crée un nouveau Pokémon dans la base de données.
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
    return {"message": "Nouveau Pokemon avec succès"}

# Met à jour les données d'un Pokémon existant dans la base de données.
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
    return {"message": "Pokemon mis à jour avec succès"}

# Supprime un Pokémon de la base de données.
def delete_pokemon(pokemon_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pokemon_type WHERE pokemon_id = %s", (pokemon_id,))
    cursor.execute("DELETE FROM pokemon_ability WHERE pokemon_id = %s", (pokemon_id,))
    cursor.execute("DELETE FROM pokemon WHERE id = %s", (pokemon_id,))
    conn.commit()
    cursor.close()
    return {"message": "Pokemon supprimé avec succès"}

# Obtient tous les Pokémon avec une pagination.
def get_all_pokemons(skip: int = 0, limit: int = 10):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemon LIMIT %s OFFSET %s", (limit, skip))
    pokemons = cursor.fetchall()
    cursor.close()
    return pokemons

# Ajoute un type à un Pokémon existant.
def add_pokemon_type(pokemon_id, type):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon_type (pokemon_id, type_id) SELECT %s, id FROM type WHERE type = %s", (pokemon_id, type))
    conn.commit()
    cursor.close()
    return {"message": "Type ajouté avec succès"}

# Ajoute une capacité à un Pokémon existant.
def add_pokemon_ability(pokemon_id, ability):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon_ability (pokemon_id, ability_id) SELECT %s, id FROM ability WHERE ability = %s", (pokemon_id, ability))
    conn.commit()
    cursor.close()
    return {"message": "Capacité ajoutée avec succès"}

# Supprime un type d'un Pokémon existant.
def delete_pokemon_type(pokemon_id, type):
    cursor = conn.cursor()
    cursor.execute("DELETE pt FROM pokemon_type pt JOIN type t ON pt.type_id = t.id WHERE pt.pokemon_id = %s AND t.type = %s", (pokemon_id, type))
    conn.commit()
    cursor.close()
    return {"message": "Type supprimé avec succès"}


# Supprime une capacité d'un Pokémon existant.
def delete_pokemon_ability(pokemon_id, ability):
    cursor = conn.cursor()
    cursor.execute("DELETE pa FROM pokemon_ability pa JOIN ability a ON pa.ability_id = a.id WHERE pa.pokemon_id = %s AND a.ability = %s", (pokemon_id, ability))
    conn.commit()
    cursor.close()
    return {"message": "Capacité supprimée avec succès"}