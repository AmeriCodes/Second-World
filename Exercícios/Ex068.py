# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
count = -1
while True:
    print('=-' * 12)
    choise = ' '
    value = int(input('Diga um valor: '))
    while choise not in 'PI':
        choise = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    pc = randint(0, 10)
    sum = pc + value
    count += 1
    if sum % 2 == 0:
        print('--' * 28)
        print(f'Você jogou {value} e o computador jogou {pc}. Total de {sum} DEU PAR')
        print('--' * 28)
        if choise in 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente. . .')
        else:
            print(f'GAME OVER! Você venceu {count} vezes.')
            break
    else:
        print('--' * 28)
        print(f'Você jogou {value} e o computador jogou {pc}. Total de {sum} DEU IMPAR')
        print('--' * 28)
        if choise in 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente. . .')
        else:
            print(f'GAME OVER! Você venceu {count} vezes.')
            break


# A resolução do professor foi.
"""
from random import randint
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0] # Esse tipo de validação me interessou, vou transpor isso para o meu código
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente. . .')
print(f'GAME OVER! Você venceu {vitoria} vezes.')
"""