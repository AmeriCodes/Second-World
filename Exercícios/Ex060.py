# Faça um programa que leia um número qualquer e mosrtre o seu fatorial.
# EX: 5! = 5 x 4 x 3 x 2 x 1= 120


# Fazendo o exercício com o 'for'
# Demorei um pouco para entender o código por que o calculo do fatorial é feito de maneira ascendente.
number = int(input('Digite um número para saber o fatorial: '))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f'O resultado de {number}! é {factorial}')


# Fazendo o exercício com o 'while'
# Já aqui, o calculo é feito de maneira descendente.
"""
number = int(input('Digite um número para calcular seu Fatorial: '))
count = number
factorial = 1
print(f'Calculando {number}! = ', end='')
while count > 0:
    print(f'{count}', end='')
    print(f' x ' if count > 1 else ' = ', end='')
    factorial = factorial * count
    count = count - 1
print(f'{factorial}')
"""

# Fazendo o exercício com uma bibliotéca
"""
from math import factorial
number = int(input('Digite um número para calcular seu Fatorial: '))
fact = factorial(number)
print(f'O Fatorial de {number} é {fact}.')
"""