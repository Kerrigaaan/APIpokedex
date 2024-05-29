from sqlalchemy.orm import Session
from . import schemas

# Obtient un Pokémon selon son identifiant dans la base de données.
def get_pokemon(db: Session, pokemon_id: int):
    return db.query(schemas.Pokemon).filter(schemas.Pokemon.id == pokemon_id).first()

# Obtient une liste de Pokémon avec une pagination.
def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(schemas.Pokemon).offset(skip).limit(limit).all()

# Crée un nouveau Pokémon dans la base de données.
def create_pokemon(db: Session, pokemon: schemas.Pokemon):
    db.add(pokemon)
    db.commit()
    db.refresh(pokemon)
    return pokemon

# Met à jour les données d'un Pokémon existant dans la base de données.
def update_pokemon(db: Session, pokemon_id: int, pokemon_data: dict):
    db_pokemon = get_pokemon(db, pokemon_id)
    if db_pokemon:
        for key, value in pokemon_data.items():
            setattr(db_pokemon, key, value)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon

# Supprime un Pokémon de la base de données.
def delete_pokemon(db: Session, pokemon_id: int):
    db_pokemon = get_pokemon(db, pokemon_id)
    if db_pokemon:
        db.delete(db_pokemon)
        db.commit()
    return db_pokemon

