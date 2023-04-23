# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('Lista dos números ímpares e múltiplos de 3.')
soma = 0
cont = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0: # Verificando se os números são divisíveis por 3 e são impares.
        soma = soma + c # também poderia ser escrito assim "soma += c"
        cont = cont + 1 # também poderia ser escrito assim "soma += 1"
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
