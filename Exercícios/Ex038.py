# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# - O primeiro número é maior
# - O segundo número é maior
# - Não existe valor maior, os dois são iguais


number_1 = int(input('Digite o primeiro número: '))
number_2 = int(input('Digite o segundo número: '))

if number_1 < number_2:
    print(f'{number_2} é o maior número.')
elif number_2 < number_1:
    print(f'{number_1} é o maior número.')
else:
    print('Os dois valores são iguais')
