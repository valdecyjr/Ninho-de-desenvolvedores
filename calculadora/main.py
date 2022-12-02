from platform import system
from os import system as st

operatores = ['+', '-', '*', '/', '**', '//']


def limpar():  # limpa a tela do terminal ou cmd
    if system() == 'Linux':
        st('clear')
    elif system() == 'Windows':
        st('cls')


def verificador(func, cache={}):
    # TODO: cloruse
    def validar_inputs(x, y):  # valida os inputs
        # tenta executar os comandos
        # se ter erro ele executa o que está dentro do except
        try:
            # se Não é passado o X ele vai usar o numero guardado em cache
            if x == 'None':
                # x vai receber o valor guardado em cache
                # y se possivel, vai ser convertido para float
                x, y = cache['value'], float(y)
            else:
                # olha se x e y podem ser convertidos em numero
                x, y = float(x), float(y)
            # cache vai receber o valor da função passada com parâmetro
            cache['value'] = func(x, y)
            # retorna o resultado
            return cache['value']
        except:
            # caso ter erro na converção de x ou y para float
            # cai dentro do except
            limpar()
            print('Digite apenas Numeros')
            input('Aperte "Enter" para continuar')
            limpar()
    return validar_inputs


@verificador
def soma(x, y):
    return x + y


@verificador
def sub(x, y):
    return x - y


@verificador
def mult(x, y):
    return x * y


@verificador
def div(x, y):
    return x / y


@verificador
def potencia(x, y):
    return x**y


@verificador
def raiz(x, y):
    # gambiarra
    y **= -1
    return potencia(x, y)


if __name__ == '__main__':
    while True:
        # enquanto nao escrever sair, no numb1 vai continuar executando
        print('Caso deseje sair, digite sair ou s quando pedir o primeiro numero')
        print('Caso queira raiz digite: "//", sem as aspas ')
        numb1 = input('Digite o primeiro numero: ')
        numb2 = input('Digite o segundo numero: ')
        if numb1 in operatores:
            # se o numb1 for um operator valido
            # ele executar o codigo com o cache sendo x
            # op vai receber o operator passado
            numb1, op = 'None', numb1
        elif numb1.lower() == 'sair' or numb1.lower() == 's':
            # se o numb1 for sair ou s ele vai parar o codigo
            break
        else:
            op = input('digite o operator: ')
        if op in operatores:
            # checa se op esta na lista operator e
            # chama a função de acordo com o operator
            if op == operatores[0]:
                print(soma(numb1, numb2))
            if op == operatores[1]:
                print(sub(numb1, numb2))
            if op == operatores[2]:
                print(mult(numb1, numb2))
            if op == operatores[3]:
                if numb2 == 0:
                    # Se o divisor for 0, mostra esse aviso
                    print('Não é possivel dividir por 0')
                else:
                    print(div(numb1, numb2))
            if op == operatores[4]:
                print(potencia(numb1, numb2))
            if op == operatores[5]:
                print(raiz(numb1, numb2))
            input('Digite "Enter" para continuar')
            limpar()
        else:
            # Caso o op nao exista na lista operatores
            # ele vai cair aqui dentro
            limpar()
            print('Operator invalido')
            input('Aperte Enter para continuar')
            limpar()
