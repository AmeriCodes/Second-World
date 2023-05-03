# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
number = int(input('Digite um número [999 para parar]: '))
count = 0
if number != 999: # Abri essa condição pois percebi que caso o usuário finalizasse o programa sem digitar nada antes, a soma daria 999.
    sum = number
else:
    sum = 0    
while number != 999:
    number = int(input('Digite um número [999 para parar]: '))
    count = count + 1
    if number != 999:
        sum = sum + number
    else:
        sum = sum + number - 999
print(f'A soma de entre os {count} números digitados foi de {sum}')
"""

