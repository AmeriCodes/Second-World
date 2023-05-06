# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mestre: 
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000.
# Qual é o nome do produto mais barato.

store_name ="CIRIC'S STORE"
print('==' * 15)
print(f'{store_name:^30}')
print('==' * 15)

total_price = plus1k = 0
cheapest = ''
low_price = 0

while True:
    
    product = str(input('Nome do produto: '))
    
    cost = float(input('Preço: R$'))
    total_price += cost
    
    if cost > 1000:
        plus1k += 1
    
    if low_price == 0 or cost < low_price: # interessante a utilização do 'or'
        low_price = cost
        cheapest = product
    
    question = ' '
    while question not in 'SN':
        question = str(input('Mais algum produto? [S/N] ')).strip().upper()[0]
    if question == 'N':
        break
    
end_name = 'FIM DO PROGRAMA'
print('{:-^40}'.format('FIM DO PROGRAMA')) # Manipulação de string interessante

print(f'O total de compra foi de R${total_price:.2f}')
print(f'Temos {plus1k} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {cheapest} que custa R${low_price:.2f}')