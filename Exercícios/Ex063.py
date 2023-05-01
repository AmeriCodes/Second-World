# Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela os 'n' primeiros elementos de uma Sequência de Fibonacci.

n = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print(f'{termo1} → {termo2}',end='')
cont = 3
while cont <= n:
    termo3 = termo1 + termo2
    print(f' → {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' → FIM')

"""
number = int(input("Digite um número inteiro: "))

fibonacci = [0, 1]  # lista inicial contendo os dois primeiros números da sequência de Fibonacci

for i in range(2, number):
    next = fibonacci[i-1] + fibonacci[i-2]  # calcula o próximo número da sequência
    fibonacci.append(next)  # adiciona o próximo número à lista

print(fibonacci[:number])  # imprime os primeiros n números da sequência de Fibonacci
"""