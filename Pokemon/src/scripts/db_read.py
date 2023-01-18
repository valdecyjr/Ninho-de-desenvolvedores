import sqlite3, io
from requests import request
from urllib.request import urlopen

def db_select(name):


    url = f"http://pokeapi.co/api/v2/pokemon/{name.lower()}/"
    response = request("GET", url)
    json = response.json()
    image = json['sprites']['front_default']
    image_stream = urlopen(image).read()
    image_file = io.BytesIO(image_stream)
    con = sqlite3.connect('pokemon.db')
    cur = con.cursor()
    busca= f"""
    SELECT name, tipo, ataque, defesa, ataque_especial, defesa_especial, hp, speed, habilidades
    FROM pokemons
    WHERE name = "{name}"
    """
    cur.execute(busca)
    dado = cur.fetchone(), image_file
    url = f"http://pokeapi.co/api/v2/pokemon/{name.lower()}/"
    con.close()
    return dado

def db_select_moves(name):
    con = sqlite3.connect('pokemon.db')
    cur = con.cursor()
    busca = f"""
    SELECT move, level
    FROM move
    WHERE name = "{name}" and move_learn_method = "level-up"
    """
    cur.execute(busca)
    dado = cur.fetchall()
    con.close()
    return dado