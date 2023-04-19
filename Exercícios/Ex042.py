# Refaça o Exercício 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

from time import sleep

print('=' * 24)
print('ANALISADOR DE TRIÂNGULOS')
print('=' * 24)
sleep(0.5)
reta_1 = float(input('Digite a primeira medida: '))
reta_2 = float(input('Digite a segunda medida: '))
reta_3 = float(input('Digite a terceira medida: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_2 + reta_1: # Verificando a possibilidade de triãngulo
    print('Os segmentos acima podem formar um triângulo ', end='')
    if reta_1 == reta_2 == reta_3:
        print('EQUILÁTERO') # Todos os lados iguais
    elif reta_1 != reta_2 != reta_3 != reta_1:
        print('ESCALENO') # Todos os lados diferentes
    else:
        print('ISÓSCELES') # Dois lados iguais
else:
    print('Os segmentos acima não formam triângulo') # Alguma reta foi maior do que a soma das outras duas.
