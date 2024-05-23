from typing import List, Optional
from .models import Pokemon
from .database import pokedex

def get_pokemon(pokemon_id: int) -> Optional[Pokemon]:
    for pokemon in pokedex:
        if pokemon["id"] == pokemon_id:
            return Pokemon(**pokemon)
    return None

def get_all_pokemons() -> List[Pokemon]:
    return [Pokemon(**data) for data in pokedex]
