import sqlite3


def create_table_pokemons():
    con = sqlite3.connect('pokemon.db')

    cur = con.cursor()

    create_table ="""
    CREATE TABLE pokemons (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL,
                        tipo TEXT NOT NULL,
                        ataque INTEGER NOT NULL,
                        defesa INTEGER NOT NULL,
                        ataque_especial INTEGER NOT NULL,
                        defesa_especial INTEGER NOT NULL,
                        hp INTEGER NOT NULL,
                        speed INTEGER NOT NULL,
                        habilidades TEXT NOT NULL)
    """

    cur.execute(create_table)

    con.commit()

    con.close()

def create_table_moves():
    con = sqlite3.connect('pokemon.db')

    cur = con.cursor()
    create_table ="""
    CREATE TABLE move (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        move TEXT NOT NULL,
                        level INTERGER NOT NULL,
                        move_learn_method TEXT NOT NULL,
                        FOREIGN KEY (name) REFERENCES pokemons(name))
    """

    cur.execute(create_table)

    con.commit()

    con.close()
    print('sucesso')

if __name__ == '__main__':
    create_table_pokemons()
    create_table_moves()