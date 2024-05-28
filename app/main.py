from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from . import database

app = FastAPI()

class Pokemon(BaseModel):
    id: int
    name: str
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    image_url: str

class UpdatePokemon(BaseModel):
    name: str = None
    hp: int = None
    attack: int = None
    defense: int = None
    sp_attack: int = None
    sp_defense: int = None
    speed: int = None
    image_url: str = None

class PokemonType(BaseModel):
    type: str

class PokemonAbility(BaseModel):
    ability: str

@app.post("/pokemons/", response_model=dict)
def create_pokemon(pokemon: Pokemon):
    return database.create_pokemon(pokemon.dict())

@app.get("/pokemons/{pokemon_id}", response_model=dict)
def read_pokemon(pokemon_id: int):
    pokemon = database.get_pokemon_by_id(pokemon_id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@app.put("/pokemons/{pokemon_id}", response_model=dict)
def update_pokemon(pokemon_id: int, pokemon: UpdatePokemon):
    return database.update_pokemon(pokemon_id, {k: v for k, v in pokemon.dict().items() if v is not None})

@app.delete("/pokemons/{pokemon_id}", response_model=dict)
def delete_pokemon_endpoint(pokemon_id: int):
    return database.delete_pokemon(pokemon_id)

@app.get("/pokemons/", response_model=list)
def read_pokemons(skip: int = 0, limit: int = 10):
    return database.get_all_pokemons(skip, limit)

@app.post("/pokemons/{pokemon_id}/types", response_model=dict)
def add_type_to_pokemon(pokemon_id: int, type: PokemonType):
    return database.add_pokemon_type(pokemon_id, type.type)

@app.post("/pokemons/{pokemon_id}/competences", response_model=dict)
def add_ability_to_pokemon(pokemon_id: int, ability: PokemonAbility):
    return database.add_pokemon_ability(pokemon_id, ability.ability)

@app.delete("/pokemons/{pokemon_id}/types", response_model=dict)
def delete_type_from_pokemon(pokemon_id: int, type: PokemonType):
    return database.delete_pokemon_type(pokemon_id, type.type)

@app.delete("/pokemons/{pokemon_id}/competences", response_model=dict)
def delete_ability_from_pokemon(pokemon_id: int, ability: PokemonAbility):
    return database.delete_pokemon_ability(pokemon_id, ability.ability)
