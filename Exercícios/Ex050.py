# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for numero in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1
print(f'A soma de todos os {cont} pares digitados é {soma}')