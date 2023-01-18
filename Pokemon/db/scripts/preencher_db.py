import requests
from time import sleep
from insert_db import *

error_pokemons = []

def pokemon(nome: str):
    try:
        url = f"http://pokeapi.co/api/v2/pokemon/{nome.lower()}/"

        response = requests.request("GET", url)
        json = response.json()
        name = json['name']
        status = {
                "ataque": 0,
                "defesa": 0,
                "ataque_especial": 0,
                "defesa_especial":0,
                "hp": 0,
                "speed": 0
            }
        for stats in json['stats']:
            if stats['stat']['name'] == 'hp':
                status['hp'] = stats['base_stat']
            if stats['stat']['name'] == 'attack':
                status['ataque'] = stats['base_stat']
            if stats['stat']['name'] == 'defense':
                status['defesa'] = stats['base_stat']
            if stats['stat']['name'] == 'special-attack':
                status['ataque_especial'] = stats['base_stat']
            if stats['stat']['name'] == 'special-defense':
                status['defesa_especial'] = stats['base_stat']
            if stats['stat']['name'] == 'speed':
                status['speed'] = stats['base_stat']
        tipo = ''
        for type in json['types']:
            tipo += " " + type['type']['name']

        habilidades = ''
        for abilities in json['abilities']:
            habilidades += " " +  abilities['ability']['name']
        insert_pokemons(name, tipo, status, habilidades)
    except:
        global error_pokemons
        error_pokemons.append(nome)
        print(f"erro em inserir {nome}")

def moves(nome: str):
    move_name = []
    level = []
    move_learn = []
    try:
        url = f"http://pokeapi.co/api/v2/pokemon/{nome.lower()}/"

        response = requests.request("GET", url)
        json = response.json()
        name = json['name']
        for moves in json['moves']:
            move_name.append(moves['move']['name'])
            level.append(moves['version_group_details'][0]['level_learned_at'])
            move_learn.append(moves['version_group_details'][0]['move_learn_method']['name'])
        
        for i in range(len(move_name)):
           insert_moves(nome, move_name[i], level[i], move_learn[i])
           print(f'movimento {move_name[i]} do pokemon {name} adicionado com sucesso')
            
    except:
        print(f"erro em inserir {nome}")

    


if __name__ == '__main__':
    pokename = open("pokemon_worldlist.txt", "r")

    for l in pokename.readlines():
        pokemon(l.strip())
        moves(l.strip())
        sleep(1)
    if len(error_pokemons) > 0:
        print('pokemons que deram error:\n', error_pokemons)
