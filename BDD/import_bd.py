import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

nom_base_de_donnees = 'pokedex'
sql_create_db = f"CREATE DATABASE IF NOT EXISTS {nom_base_de_donnees}"

try:
    cursor.execute(sql_create_db)
    print("La base de données a été créée avec succès ou existait déjà!")
except Exception as e:
    print("Une erreur s'est produite lors de la création de la base de données:", e)

cursor.close()
conn.close()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=nom_base_de_donnees
)

cursor = conn.cursor()

chemin_fichier_sql = "BDD/pokemons.sql"

try:
    with open(chemin_fichier_sql, 'r') as fichier_sql:
        sql_statements = fichier_sql.read()

    sql_commands = sql_statements.split(';')

    for command in sql_commands:
        command = command.strip()
        if command:
            cursor.execute(command)

    conn.commit()

    print("Le fichier SQL a été importé avec succès!")
except Exception as e:
    print("Une erreur s'est produite lors de l'importation du fichier SQL:", e)

cursor.close()
conn.close()

