# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from .CRUD import get_pokemon, get_all_pokemons
from .schemas import PokemonResponse

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/api/pokemons", response_model=list[PokemonResponse])
def read_pokemons():
    return get_all_pokemons()

@app.get("/api/pokemons/{pokemon_id}", response_model=PokemonResponse)
def read_pokemon(pokemon_id: int):
    pokemon = get_pokemon(pokemon_id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    pokemons = get_all_pokemons()
    return templates.TemplateResponse("index.html", {"request": request, "pokemons": pokemons})
