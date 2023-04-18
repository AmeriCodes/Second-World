# Escreva um programa para o empréstimo bancário de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('=+' * 20)
print('Analisador de financiamento de casas.')
print('=-' * 20)

valor_casa = float(input('Digite o valor do imóvel desejado R$ '))
salario = float(input('Digite o valor do seu salário R$ '))
anos = int(input('Digite em quanto anos quitar a dívida: '))
meses = anos * 12

prestacao_mensal = valor_casa / meses
prestacao_maxima = (salario * 30) / 100

if prestacao_mensal > prestacao_maxima:
    print('Infelizmente você não pode financiar esse imóvel.')
    print(f'A prestação mensal ficaria de R${prestacao_mensal:.2f}, ultrapassando R${prestacao_maxima:.2f} que seria 30% do seu salário.')
    sugestao = valor_casa // prestacao_maxima # O valor da casa dividido pela prestação máxima, teremos a quantidade de messes adequada.
    possibilidade_em_anos = sugestao // 12 # Conversão para anos
    print(f'Para financiar uma casa no valor R${valor_casa:.2f} com o seu salário. \nSeria necessário aumentar o tempo de quitação para {possibilidade_em_anos:.0f} anos.')
    nova_prestacao_mensal = valor_casa // sugestao # Uma prestação possível
    print(f'O qual redusiria a dívida mensal de R${prestacao_mensal:.2f} para {nova_prestacao_mensal:.2f}')
else:
    print('Este financiamento pode ser realizado.')
    print(f'Sua parcela mensal seria de R${prestacao_mensal:.2f}.')
