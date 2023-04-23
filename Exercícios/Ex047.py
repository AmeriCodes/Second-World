# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Lista dos número pares de 1 até 50')
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')

# Inicialmente eu fiz assim
"""
for n in range(1, 51):
    if n %2 == 0:
        print(n, end=' ')
print('Acabou')
"""
# O problema é que desse jeito há o dobro de iterações.
