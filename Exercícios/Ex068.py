# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
count = -1
while True:
    print('=-' * 12)
    value = int(input('Diga um valor: '))
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