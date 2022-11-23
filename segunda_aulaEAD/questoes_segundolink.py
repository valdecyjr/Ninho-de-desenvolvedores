from platform import system
from os import system as st
from numbers import Number
from random import randint


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
        print(func.__doc__)
        return func(*args)
    return execucao

@exibir
def questao1():
    """
Questão:Write a Python program to find those
         numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
    """
    cache = []
    for i in range(1500,2701):
        if i%7==0 and i%5==0:
            cache.append(i)
    print(cache)
    endfunc()


@exibir
def questao2():
    """
Questão: Write a Python program to convert temperatures to and
         from celsius, fahrenheit
         Expected Output:
         60ºC is 140 in Fahrenheit
         45ºF is 7 in Celsius
    """
    temperatura = input('Digite o valor temperatura: ')
    escala = input('A Escala é Celsius ou Fahrenheit? : ')
    if isinstance(int(temperatura), Number):
        if escala.lower() == 'celsius':
            print(f'{temperatura}ºC is {(int(temperatura) * 9/5) + 32} in Fahrenheit')
        elif escala.lower() == 'fahrenheit':
            print(f'{temperatura}ºF is {(int(temperatura) - 32) * 5/9} in Celsius')  
        else:
            print('Escala informada invalida')
    else:
        print('Temperatura informada invalida')
    endfunc()


@exibir
def questao3():
    """
Questão: Write a Python program to guess a number between 1 to 9.

Note : User is prompted to enter a guess.
If the user guesses wrong then the prompt appears again until the guess is correct,
on successful guess, user will get a "Well guessed!" message, and the program will exit.
    """
    n = randint(1, 9)
    while True:
        guess = input('Insira um palpite: ')
        if isinstance(int(guess), Number) and (int(guess) > 0 and int(guess) < 10):
            if int(guess) == n:
                print('Well guessed')
                endfunc()
                break
        else:
            print('So é valido numero de 1 a 9')

@exibir
def questao4():
    """
Questão: Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
    """
    for i in range(5):
        for j in range(i):
            print('*', end = ' ')
        print('')
    for i in range(5,0, -1):
        for j in range(i):
            print('*', end= ' ')
        print('')
    endfunc()
    
@exibir
def questao5():
    """
Questão: Write a Python program that accepts a word from the user and reverse it.
    """
    word = input('Digite uma palavra: ')
    word = word[::-1]
    print(f'A palavra invertida é word')
    endfunc()


@exibir
def questao6():
    """
Questão: Write a Python program to count the number of even and odd numbers from a series of numbers.

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
    """
    count_impar = 0
    impar = []
    par = []
    count_par = 0
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    for numero in numbers:
        if numero%2 == 0:
            count_par +=1
            par.append(numero)
        else:
            count_impar += 1
            impar.append(numero)
    print(f"""
Number of even numbers : {count_impar}
Number of odd numbers : {count_par}
          """)


def questao7():
    """
Questão: Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    """
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    for item in datalist:
        print(f'O item {item}, é do tipo {type(item)}')

@exibir
def questao9():
    """
Questão: Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
    Note : The Fibonacci Sequence is the series of numbers :
    0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
    """
    i,p,a,n = 0, 0, 0, 0
    lista = []
    while i < 50:
        if i == 0:
            lista.append(i)
            i+= 1
        elif i == 1 and len(lista) < 2:
            lista.append(i)
            i += 1
        else:
            n = len(lista)
            p = lista[n-2]
            a = lista[n-1]
            i = p+a
            lista.append(i)
    for n in lista:
        print(n, end = ' ')
    print('')


if __name__ == "__main__":
    questao1() 
    questao2()
    questao3()
    questao4()
    questao5()
    questao6()
    questao7()
    questao9()
