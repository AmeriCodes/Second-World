# Crie um programa que leia dois valores e mostre um menu na tela:
"""
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
"""
# Seu programa deverá realizar a operação solicitada em casa caso.

from time import sleep
first_value = int(input('Primeiro valor: '))
second_value = int(input('Segundo valor: '))
choise = 0
while choise != 5:
    print("""    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa""")
    choise = int(input('>>>>> Qual a sua opção? '))
    if choise == 1:
        print(f'A soma entre {first_value} + {second_value} é {first_value + second_value}')
        print('=+' * 13)
        sleep(2.5)
    elif choise == 2:
        print(f'O resultado de {first_value} x {second_value} é {first_value * second_value}')
        print('x=' * 13)
        sleep(2.5)
    elif choise == 3:
        if first_value > second_value:
            bigger = first_value
            print(f'Entre {first_value} e {second_value} o maior é {bigger}')
        elif second_value > first_value:
            bigger = second_value
            print(f'Entre {first_value} e {second_value} o maior é {bigger}')
        else:
            print('Não há maior, os números não iguais.')
        print('>=' * 13)
        sleep(2.5)
    elif choise == 4:
        first_value = int(input('Primeiro valor: '))
        second_value = int(input('Segundo valor: '))
        sleep(1)
    elif choise == 5:
        print('Finalizando. . .')
        print('=-' * 13)
        sleep(2.5)
    else:
        print('Opção inválida, tente novamente.')
        sleep(2.5)
print('Fim do programa! Volte sempre!')
