from platform import system
from os import system as st


def endfunc():
    print('\n')
    input('Digite "Enter" para continuar')
    limpar()


def limpar():
    if system() == 'Linux':
        st('clear')
    elif system() == 'Windows':
        st('cls')


def exibir(func):  # closure
    def execucao(*args):
        limpar()
        print(f'Questão: {func.__doc__}')
        return func(*args)
    return execucao


@exibir
def questao1():
    """
    Fazer um programa que imprima a média aritmética dos
    números 8,9 e 7. A média dos números 4, 5 e 6. A soma das
    duas médias. A media das medias.
    """
    notas1, notas2 = [8, 9, 7], [4, 5, 6]
    media1 = sum(notas1)/3
    media2 = sum(notas2)/3
    somadasmedias = media1 + media2

    print(f"""Respostas:
As notas são: {notas1}, a media dessas notas é:{media1}
As notas são {notas2}, a media dessas notas é: {media2}
A soma das medias é: {somadasmedias}""")
    endfunc()


@exibir
def questao2():
    """
    Ler um ano de nascimento e ano atual. Imprimir a idade da
    pessoa. Se a idade for maior ou igual a 18 leia o nome da
    pessoa e imprima o nome digitado e uma mensagem
    informando que sua entrada é permitida. (Ex: Fulano, sua
    entrada foi permitida.)
    """
    nome = input('Informe seu nome: ')
    nascimento = int(input('Somente o ano que você nasceu(No formato yyyy): '))
    atual = int(input('Digite o valor do ano atual(No formato yyyy): '))

    print(f'Resposta:\n{nome}, sua entrada é permitida' if atual-nascimento >= 18
          else f'Resposta:\n {nome}, sua entrada é negada')
    endfunc()


@exibir
def questao3():
    """
    Solicitar salário, prestação. Se prestação for maior que 20%
    do salário, imprimir : Empréstimo não pode ser concedido.
    Senão imprimir Empréstimo pode ser concedido.
    """
    salario = float(input('Digite o salário: '))
    prestacao = float(input('Digite a prestacao: '))

    print('Resposta:\nEmpréstimo pode ser concedido' if prestacao <= salario * 0.2
          else 'Resposta:\nEmpréstimo não pode ser concedido')
    endfunc()


@exibir
def questao4():
    """
    Determinar o fatorial de 6, 5, 4. Determinar valores a partir
    da operação de potenciação.
    """
    fatorial = 1
    numeros = [6, 5, 4]
    print('Resposta:')
    for n in numeros:
        for i in range(1, n+1):
            fatorial *= i

        print(f'fatorial de {n} é : {fatorial}')
        fatorial = 1
    endfunc()


@exibir
def questao5():
    """
    Informar um número e imprimir se é par ou
    ímpar.
    """
    numero = int(input('Digite um numero inteiro: '))
    print('Resposta:\npar' if numero % 2 == 0
          else 'Resposta:\nimpar')
    endfunc()


@exibir
def questao6():
    """
    Ler 1 número. Se positivo, imprimir raiz quadrada
    senão o quadrado do número.
    """
    x = float(input('Digite um numero: '))
    print(f'Resposta:\n{x ** 0.5}' if x > 0
          else f'Resposta\n{x ** 2}')
    endfunc()


@exibir
def questao7():
    """
    Ler um número e imprimir igual a 20, menor que
    20, maior que 20.
    """
    numero = int(input('Digite um numero: '))
    print('Resposta:\nigual a 20' if numero == 20
          else ('Resposta:\nmenor que 20' if numero < 20
                else 'Resposta:\nmaior que 20'))
    endfunc()


@exibir
def questao8():
    """
    Crie um algoritmo que receba 3 números e
    informe qual o maior entre eles.
    """
    numero = []
    while len(numero) < 3:
        numero.append(int(input(f'Digite um o {len(numero) + 1}º numero: ')))
    numero.sort(reverse=True)
    print(f'Resposta:\nO maior número é: {numero[0]}')
    endfunc()


@exibir
def questao9():
    """
    Faça um algoritmo que leia dois números nas variáveis
    NumA e NumB, nessa ordem, e imprima em ordem inversa, isto
    é, se os dados lidos forem NumA = 5 e NumB = 9, por exemplo,
    devem ser impressos na ordem NumA = 9 e NumB = 5.
    """
    numA = int(input('Digite o NumA: '))
    numB = int(input('Digite o NumB: '))
    numA, numB = numB, numA
    print(f'NumA: {numA} \nNumB: {numB}')
    endfunc()


@exibir
def questao10():
    """
    Faça um algoritmo que leia dois números e indique se são
    iguais ou se são diferentes. Mostre o maior e o menor (nesta
    sequência).
    """
    numb1 = int(input('Digite um numero: '))
    numb2 = int(input('Digite um numero: '))
    print('Resposta:\nSão iguais' if numb1 == numb2
          else 'São diferentes')
    print(f'{numb1} {numb2}' if numb1 > numb2
          else f'{numb2} {numb1}')
    endfunc()


if __name__ == '__main__':
    questao1()
    questao2()
    questao3()
    questao4()
    questao5()
    questao6()
    questao7()
    questao8()
    questao9()
    questao10()
