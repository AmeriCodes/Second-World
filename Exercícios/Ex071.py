# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caisa possue cédulas de 50, 20, 10, 1 reais.

print('=' * 30)
print('{:^30}'.format("CIRIAC'S BANK"))
print('=' * 30)

value = int(input('Que valor você quer sacar? R$'))
total = value
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('=' * 30)
print("Volte sempre ao CIRIAC'S BANK! Tenha um bom dia!")