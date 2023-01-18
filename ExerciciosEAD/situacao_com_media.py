x = 0
nota = []
while x < 4:
    aux = float(input(f'Digite a {x+1}º nota: '))
    if aux >= 0 and aux <= 10:
        nota.append(aux)
        x += 1
    else:
        print('Nota invalida')

media = sum(nota)/4

print(f'Aluno foi aprovado com media: {media} ' if media >= 5
      else f'Aluno não foi aprovado com media: {media}')
