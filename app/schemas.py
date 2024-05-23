# app/schemas.py
from pydantic import BaseModel
from typing import List

class BaseStatsResponse(BaseModel):
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int

class PokemonResponse(BaseModel):
    id: int
    name: str
    type: List[str]
    abilities: List[str]
    base_stats: BaseStatsResponse
    image_url: str

    class Config:
        orm_mode = True
