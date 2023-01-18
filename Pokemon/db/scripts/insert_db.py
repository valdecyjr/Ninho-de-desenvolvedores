import sqlite3
import requests



def insert_pokemons(name,type,stats,habilidades):

    con = sqlite3.connect('pokemon.db')

    cur = con.cursor()

    insert_table= f"""
    INSERT INTO pokemons(name, tipo, ataque, defesa, ataque_especial, defesa_especial, hp, speed, habilidades)  
        VALUES('{name}', '{type}', '{stats['ataque']}', '{stats['defesa']}', '{stats['ataque_especial']}', '{stats['defesa_especial']}',
               '{stats['hp']}', '{stats['speed']}', '{habilidades}')        
    """
    cur.execute(insert_table) 
    con.commit()
    con.close()
    print(f'{name} inserido com sucesso')

def insert_moves(name, move , level, move_learn_method):
    con = sqlite3.connect('pokemon.db')

    cur = con.cursor()


    insert_table= f"""
        INSERT INTO move(name, move, level, move_learn_method)  
        VALUES("{name}", "{move}", "{level}", "{move_learn_method}")
        """

    cur.execute(insert_table)
    con.commit()

    con.close()