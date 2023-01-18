maior, x = None, None

while x != 0:
    if isinstance(maior, float):
        x = float(input('Digite um numero positivo maior que zero: '))
        if x >= 0:
            if x > maior:
                maior = x
            print(f'O maior numero é: {maior}')
        else:
            print(f'{x} é menor que 0')
    else:
        x = float(input('Digite um numero positivo maior que zero: '))
        if x >= 0:
            maior = x
            print(f'{maior} agora é o Maior numero')
        else:
            print(f'{x} é menor que 0')
