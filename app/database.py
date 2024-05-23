# app/database.py
import json
from typing import Dict, Any

def load_data() -> Dict[str, Any]:
    with open("data/pokelist.json", "r") as f:
        return json.load(f)

pokedex = load_data()["pokemons"]
