# Melhores o exercício 61 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

from time import sleep
print('Gerador de PA')
print('-=' * 12)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')