import pygame
from scripts.db_read import db_select_moves
class Pokemon:

    """Classe que seta meus pokemons"""

    def __init__(self, *args) -> None:
        self.nome = args[0][0][0]
        self.apelido = None
        self.level= 1
        self.xp = 0
        self.tipo = args[0][0][1]
        self.image = pygame.image.load(args[0][1])
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width*2, height*2))
        self.moves = Moves(self)
        self.stats = {
            "ataque": args[0][0][2],
            "defesa": args[0][0][3],
            "ataque_especial": args[0][0][4],
            "defesa_especial":args[0][0][5],
            "max_hp": args[0][0][6],
            "hp": args[0][0][6],
            "speed": args[0][0][7],
            "habilidades": args[0][0][8]
        }
        self.moves_aprendidos, self.moves_power, self.moves_mp = self.moves_iniciais()

    def moves_iniciais(self):
        self.moves_aprendidos = []
        moves_iniciais, level = self.moves.get_moves()
        mp = 15
        moves_aprendidos = []
        moves_power = []
        moves_mp = []
        for moves in moves_iniciais:
            moves_aprendidos.append(moves)
            power = self.stats['ataque'] * 1.20 * (level/100 + 1)
            moves_power.append(power)
            moves_mp.append(mp)
        return moves_aprendidos, moves_power, moves_mp

    def set_apelido(self, apelido):
        self.apelido = apelido

    def set_hp(self, hp):
        self.hp = hp

    def level_up(self):
        self.moves.update_pokemon(self)
        self.update_moves()
        self.stats["ataque"] = (self.stats['ataque']* 1.2 * (self.level/100 + 1)).__ceil__()
        self.stats["defesa"] = (self.stats['defesa']* 1.2 * (self.level/100 + 1)).__ceil__()
        self.stats["hp"] = (self.stats['hp']* 1.2 * (self.level/100 + 1)).__ceil__()

    def update_moves(self):
        self.moves_aprendidos = []
        new_moves, level = self.moves.get_moves()
        mp = 15
        moves_aprendidos = []
        moves_power = []
        moves_mp = []
        for moves in new_moves:
            if len(self.moves_aprendidos)<4:
                moves_aprendidos.append(moves)
                power = self.stats['ataque'] * 1.20 * (level/100 + 1)
                moves_power.append(power)
                moves_mp.append(mp)
            else:
                pass
        return moves_aprendidos, moves_power, moves_mp

class Moves():
    '''clase que guarda as habildiade do meu pokemon'''
    def __init__(self, pokemon: Pokemon) -> None:
        self.pokemon = pokemon
        self.moves = db_select_moves(self.pokemon.nome)
    
    def update_pokemon(self, pokemon: Pokemon):
        self.pokemon = pokemon
    
    def get_moves(self):
        moves_return = []
        for item in self.moves:
            if item[0] not in self.pokemon.moves_aprendidos:
                if item[1] <= self.pokemon.level:
                    level = item[1]
                    moves_return.append(item[0])
        return moves_return, level


class Tipo_Agua(Pokemon):
    def __init__(self, image, nome, hp, ataque, defesa, habilidades, crescimento, level=1) -> None:
        super().__init__(image, nome, hp, ataque, defesa, habilidades, crescimento, level)

class Tipo_Fogo(Pokemon):
    def __init__(self, image, nome, hp, ataque, defesa, habilidades, crescimento, level=1) -> None:
        super().__init__(image, nome, hp, ataque, defesa, habilidades, crescimento, level)
        pass

class Tipo_Terra(Pokemon):
    def __init__(self, image, nome, hp, ataque, defesa, habilidades, crescimento, level=1) -> None:
        super().__init__(image, nome, hp, ataque, defesa, habilidades, crescimento, level)
        pass

class Tipo_Normal(Pokemon):
    def __init__(self, image, nome, hp, ataque, defesa, habilidades, crescimento, level=1) -> None:
        super().__init__(image, nome, hp, ataque, defesa, habilidades, crescimento, level)
        pass