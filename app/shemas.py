# app/schemas.py
from pydantic import BaseModel

class PokemonBase(BaseModel):
    name: str
    type: str
    description: str

class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True
