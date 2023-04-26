# Melhore o jogo do exercício 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Abaixo da minha resposta, deixarei a resolução do professor do curso, pois tem algumas alterações interessantes, como a utilização de operadores booleanos.

from random import randint
count = 1
print('Em que número penso [0/10]?')
pc = randint(0, 10)
player = int(input('Digite aqui: '))
while pc != player:
    count = count + 1
    player = int(input('Tente novamente: '))
if count < 2:
    print(f'Incrível, com essa sorte, você deveria jogar na loteria!')
elif count < 6:
    print(f'Você conseguiu, com apenas {count} tentarivas.')
elif count < 9:
    print(f'Você só acertou na {count}º tentativa,')
else:
    print(f'Vigi Maria! Você acertou com {count} tentativas, espero que você nunca dependa de sorte na sua vida. . .')
 

"""
from random import randint
computador = randint(0, 10)
print('Sou seu computador. . . Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False # Utilização de Booleanos.
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1 # isso é igual a 'palpite = palpite + 1'.
    if jogador == computador:
        acertou = True # Utilização de Booleanos.
    else:
        if jogador < computador:
            print('Mais. . . Tente mais uma vez.')
        elif jogador > computador:
            print('Menos. . . Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
"""
