from platform import system
from os import system as st

operatores = ['+', '-', '*', '/', '**', '//']


def limpar():
    if system() == 'Linux':
        st('clear')
    elif system() == 'Windows':
        st('cls')


def verificador(func, cache={}):
    def validar_inputs(x, y):
        try:
            if x == 'None':
                x, y = cache['value'], float(y)
            else:
                x, y = float(x), float(y)

            cache['value'] = func(x, y)
            return cache['value']
        except:
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
    y **= -1
    return potencia(x, y)


if __name__ == '__main__':
    while True:
        print('Caso deseje sair, digite sair ou s quando pedir o primeiro numero')
        print('Caso queira raiz digite: "//", sem as aspas ')
        numb1 = input('Digite o primeiro numero: ')
        numb2 = input('Digite o segundo numero: ')
        if numb1 in operatores:
            numb1, op = 'None', numb1
        elif numb1.lower() == 'sair' or numb1.lower() == 's':
            break
        else:
            op = input('digite o operator: ')
        if op in operatores:
            if op == operatores[0]:
                print(soma(numb1, numb2))
            if op == operatores[1]:
                print(sub(numb1, numb2))
            if op == operatores[2]:
                print(mult(numb1, numb2))
            if op == operatores[3]:
                if numb2 == 0:
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
            limpar()
            print('Operator invalido')
            input('Aperte Enter para continuar')
            limpar()
