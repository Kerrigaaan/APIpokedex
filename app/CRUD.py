from sqlalchemy.orm import Session
from . import models

def get_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()

def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()

def create_pokemon(db: Session, pokemon: models.Pokemon):
    db.add(pokemon)
    db.commit()
    db.refresh(pokemon)
    return pokemon

def update_pokemon(db: Session, pokemon_id: int, pokemon_data: dict):
    db_pokemon = get_pokemon(db, pokemon_id)
    if db_pokemon:
        for key, value in pokemon_data.items():
            setattr(db_pokemon, key, value)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon

def delete_pokemon(db: Session, pokemon_id: int):
    db_pokemon = get_pokemon(db, pokemon_id)
    if db_pokemon:
        db.delete(db_pokemon)
        db.commit()
    return db_pokemon

