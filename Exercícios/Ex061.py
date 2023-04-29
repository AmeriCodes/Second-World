# Refaça o Exercício 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA')
print('-=' * 12)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
print('FIM')
