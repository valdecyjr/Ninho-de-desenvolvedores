p = None
sexo = input('Digite o seu sexo F ou M: ')
a = float(input('Digite a sua altura: '))
if sexo.lower() == 'f':
    p = (62.1 * a) - 44.7
elif sexo.lower() == 'm':
    p = (72.7 * a) - 58
else:
    print('Digite um sexo válido')

if isinstance(p, float):
    print(f"Seu peso ideal é: {p} ")
