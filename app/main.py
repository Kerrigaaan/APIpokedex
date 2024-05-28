from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
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

@app.post("/pokemons/{pokemon_id}/types", response_model=dict)
def add_type_to_pokemon(pokemon_id: int, type: PokemonType):
    return database.add_pokemon_type(pokemon_id, type.type)

@app.post("/pokemons/{pokemon_id}/abilities", response_model=dict)
def add_ability_to_pokemon(pokemon_id: int, ability: PokemonAbility):
    return database.add_pokemon_ability(pokemon_id, ability.ability)

@app.post("/pokemons/comments/{pokemon_id}/", response_model=dict)
async def add_comment_to_pokemon(pokemon_id: int, comment: str):
    """
    Add a comment to a Pokémon.
    """
    return database.add_comment_to_pokemon(pokemon_id, comment)

@app.post("/pokemons/{pokemon_id}/favorite/", response_model=dict)
async def add_pokemon_to_favorites(pokemon_id: int):
    """
    Add a Pokémon to favorites.
    """
    return database.add_pokemon_to_favorites(pokemon_id)

@app.get("/pokemons/{pokemon_id}", response_model=dict)
def read_pokemon(pokemon_id: int):
    pokemon = database.get_pokemon_by_id(pokemon_id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@app.get("/pokemons/", response_model=list)
def read_pokemons(skip: int = 0, limit: int = 10):
    return database.get_all_pokemons(skip, limit)

@app.get("/pokemons/search/{pokemon_name}", response_model=List[Pokemon])
def search_pokemon_by_name(pokemon_name: str):
    return database.search_pokemon_by_name(pokemon_name)

@app.get("/types/", response_model=List[str])
def get_all_pokemon_types():
    return database.get_all_pokemon_types()

@app.get("/abilities/", response_model=List[str])
def get_all_pokemon_abilities():
    return database.get_all_pokemon_abilities()

@app.get("/pokemons/type/{type_name}", response_model=List[Pokemon])
def search_pokemon_by_type(type_name: str):
    return database.search_pokemon_by_type(type_name)

@app.get("/pokemons/ability/{ability_name}", response_model=List[Pokemon])
def search_pokemon_by_ability(ability_name: str):
    return database.search_pokemon_by_ability(ability_name)

@app.get("/pokemons/{pokemon_id}/abilities", response_model=List[str])
def get_pokemon_abilities(pokemon_id: int):
    return database.get_pokemon_abilities(pokemon_id)

@app.get("/pokemons/{pokemon_id}/types", response_model=List[str])
def get_pokemon_types(pokemon_id: int):
    return database.get_pokemon_types(pokemon_id)

@app.get("/pokemons/stats", response_model=dict)
def get_pokemon_stats():
    return database.get_pokemon_stats()

@app.get("/pokemons/random", response_model=Pokemon)
def get_random_pokemon():
    return database.get_random_pokemon()

@app.get("/pokemons/count", response_model=dict)
def get_pokemon_count():
    return database.get_pokemon_count()

@app.get("/pokemons/strongest", response_model=List[Pokemon])
def get_strongest_pokemons(top: int = 10):
    return database.get_strongest_pokemons(top)

@app.get("/pokemons/weakest", response_model=List[Pokemon])
def get_weakest_pokemons(top: int = 10):
    return database.get_weakest_pokemons(top)

@app.get("/pokemons/evolution-chain/{pokemon_id}", response_model=List[Pokemon])
def get_evolution_chain(pokemon_id: int):
    return database.get_evolution_chain(pokemon_id)

@app.get("/pokemons/move/{move_name}", response_model=List[Pokemon])
def get_pokemon_by_move(move_name: str):
    return database.get_pokemon_by_move(move_name)

@app.get("/pokemons/search/", response_model=list)
async def search_pokemon_by_type(types: str = Query(..., title="Type(s) of Pokémon")):
    """
    Search Pokémon by type(s).
    """
    type_list = types.split(",")
    return database.search_pokemon_by_type(type_list)

@app.get("/pokemons/filter/", response_model=list)
async def filter_pokemon_by_stats(min_hp: int = None, max_hp: int = None,
                                  min_attack: int = None, max_attack: int = None,
                                  min_defense: int = None, max_defense: int = None,
                                  min_sp_attack: int = None, max_sp_attack: int = None,
                                  min_sp_defense: int = None, max_sp_defense: int = None,
                                  min_speed: int = None, max_speed: int = None,
                                  limit: int = 10):
    """
    Filter Pokémon by statistics.
    """
    return database.filter_pokemon_by_stats(min_hp, max_hp,
                                            min_attack, max_attack,
                                            min_defense, max_defense,
                                            min_sp_attack, max_sp_attack,
                                            min_sp_defense, max_sp_defense,
                                            min_speed, max_speed,
                                            limit)

@app.get("/pokemons/search/name/", response_model=list)
async def search_pokemon_by_name(name: str = Query(..., title="Name of Pokémon")):
    """
    Search Pokémon by name.
    """
    return database.search_pokemon_by_name(name)

@app.get("/pokemons/comments/{pokemon_id}/", response_model=list)
async def get_pokemon_comments(pokemon_id: int):
    """
    Get comments for a Pokémon.
    """
    return database.get_pokemon_comments(pokemon_id)

@app.get("/pokemons/favorites/", response_model=list)
async def get_favorite_pokemons():
    """
    Get favorite Pokémon.
    """
    return database.get_favorite_pokemons()

@app.put("/pokemons/{pokemon_id}", response_model=dict)
def update_pokemon(pokemon_id: int, pokemon: UpdatePokemon):
    return database.update_pokemon(pokemon_id, {k: v for k, v in pokemon.dict().items() if v is not None})

@app.delete("/pokemons/{pokemon_id}", response_model=dict)
def delete_pokemon_endpoint(pokemon_id: int):
    return database.delete_pokemon(pokemon_id)

@app.delete("/pokemons/{pokemon_id}/types", response_model=dict)
def delete_type_from_pokemon(pokemon_id: int, type: PokemonType):
    return database.delete_pokemon_type(pokemon_id, type.type)

@app.delete("/pokemons/{pokemon_id}/abilities", response_model=dict)
def delete_ability_from_pokemon(pokemon_id: int, ability: PokemonAbility):
    return database.delete_pokemon_ability(pokemon_id, ability.ability)


