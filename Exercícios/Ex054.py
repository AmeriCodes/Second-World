# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
for pess in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {pess}º pessoa: '))
    idade = ano_atual - nasc
    if idade >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1
print(f'Ao todo tivemos {maiores} maiores, e {menores} menores de idade')