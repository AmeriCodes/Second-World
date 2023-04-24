# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.


count = 0 # Uso essa variável para contar as idades depois tirar a média.
average = 0 # Uso essa variável para tirar a média.
older_man = 0 # 
older_name = ''
for peaple in range(1,5):
    print(f'===== {peaple}ª PESSOA =====')
    name = str(input('NOME: ')).strip()
    years_old = int(input('IDADE: '))
    sex = str(input('SEXO [M/F]: ')).strip()
    count = count + years_old
    if peaple == 1 and sex in 'Mm':
        older_man = years_old
        older_name = name
    if sex in 'Mm' and years_old > older_man:
        older_man = years_old
        older_name = name
average = count / 4
print(f'A média de idade do grupo é de {average}')
print(f'O homem mais velho tem {older_man} anos e se chama {older_name}.')
