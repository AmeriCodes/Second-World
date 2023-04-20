# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

player = int(input('Qual sua jogada: '))
pc = randint(0, 2)
options = ('PEDRA', 'PAPEL', 'TESOURA')

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('-=' * 13)

if player in [0, 1, 2]:
    print(f'O Computador jogou {options[pc]}')
    print(f'Jogador jogou {options[player]}')
    print('-=' * 13)

    if pc == player:
        print('EMPATE')
    elif pc == 0 and player == 1 or pc == 1 and player == 2 or pc == 2 and player == 0:
        print('JOGADOR VENCE')
    elif player == 0 and pc == 1 or player == 1 and pc == 2 or player == 2 and pc == 0:
        print('COMPUTADOR VENCE')
else:
    print('JOGADA INVÁLIDA')
