# Escreva um programa para o empréstimo bancário de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('=+' * 20)
print('Analisador de financiamento de casas.')
print('=-' * 20)

valor_casa = float(input('Digite o valor do imóvel desejado R$ '))
salário = float(input('Digite o valor do seu salário R$ '))
anos = int(input('Digite em quanto anos quitar a dívida: '))
meses = anos * 12

prestação_mensal = valor_casa / meses
prestação_máxima = (salário * 30) / 100

if prestação_mensal > prestação_máxima:
    print('Infelizmente você não pode financiar esse imóvel.')
    print(f'A prestação mensal ficaria de R${prestação_mensal:.2f}, ultrapassando R${prestação_máxima:.2f} que seria 30% do seu salário.')
    sugestão = valor_casa // prestação_máxima # O valor da casa dividido pela prestação máxima, teremos a quantidade de messes adequada.
    possibilidade_em_anos = sugestão // 12 # Conversão para anos
    print(f'Para financiar uma casa no valor R${valor_casa:.2f} com o seu salário. \nSeria necessário aumentar o tempo de quitação para {possibilidade_em_anos:.0f} anos.')
    nova_prestação_mensal = valor_casa // sugestão # Uma prestação possível
    print(f'O qual redusiria a dívida mensal de R${prestação_mensal:.2f} para {nova_prestação_mensal:.2f}')
else:
    print('Este financiamento pode ser realizado.')
    print(f'Sua parcela mensal seria de R${prestação_mensal:.2f}.')
