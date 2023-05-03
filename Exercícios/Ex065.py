# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. 



value = int(input('Digite um número: '))
question = str(input('Quer continuar? [S/N] ')).strip().upper()

average = 0
count = 1
bigger = smaller = sum = value

while question in 'Ss':
    count += 1
    new_value = int(input('Digite um número: '))
    question = str(input('Quer continuar? [S/N] ')).strip().upper()
    sum += new_value
    average = sum / count
    if new_value > value:
        bigger = new_value
    else:
        smaller = new_value
print(f'Você digitou {count} números e a média foi {average:.2f}')
print(f'O maior valor foi {bigger} e o menor foi {smaller}')


# Está foi a resposta do professor
"""
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
"""
