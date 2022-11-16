sala = float(input('Digite o valor do salario: '))
financ = float(input('Digite o valor do Financiamento pretendido: '))

print('Financiamento concendido, obrigado por nos consultar'
      if financ <= 5 * sala else
      'Financiamento negado, obrigado por nos consultar')
