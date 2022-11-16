nota, cache = [], []
x = 0

while x < 5:
    aux = float(input(f'Digite a {x+1}º nota: '))
    if aux >= 0 and aux <= 10:
        nota.append(aux)
        x += 1

media = sum(nota)/5
for n in nota:
    if n > media:
        cache.append(n)

print(f"""
A soma das notas é: {sum(nota)}
A média das notas é: {media}
Os valores maiores que a média são: {cache}
      """)
