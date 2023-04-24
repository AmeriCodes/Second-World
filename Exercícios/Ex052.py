# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite o número: '))
total = 0
for c in range(1, numero + 1): # numero + 1, pois no range, é ignorado o último número, sendo necessário acrescentar mais 1.
    if numero % c == 0: # testando se os números do range, resultam numa divisão perfeita.
        total = total + 1 # contando quantos números de 1 até o próprio tem divisão perfeita.
        print(c, end=', ') # mostrando os números na condição do 'if' horizontalmente.
print(f'São os números que dividem {numero}')
print(f'O número {numero} foi dividido {total} vezes.')
if total == 2: # números primos são divisíveis por eles mesmo e por 1, não sendo isso não são primos.
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')
