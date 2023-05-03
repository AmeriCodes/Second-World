# Crie um programa que leia vários números interios pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

count = sum = 0

while True:
    value = int(input('Digite um valor: '))
    if value == 999:
        break
    count += 1
    sum += value
print(f'Foram digitados um total de {count} números e a soma entre eles resultou em {sum}')
