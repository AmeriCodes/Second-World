# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. 

average = 0
count = 1

value = int(input('Digite um número: '))
question = str(input('Quer continuar? [S/N] ')).strip().upper()

bigger = smaller = value
sum = value

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
