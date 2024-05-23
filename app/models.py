# app/models.py
from pydantic import BaseModel
from typing import List, Dict

class BaseStats(BaseModel):
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int

class Pokemon(BaseModel):
    id: int
    name: str
    type: List[str]
    abilities: List[str]
    base_stats: BaseStats
    image_url: str
