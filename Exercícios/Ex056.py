# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.


count = 0 # Uso essa variável para contar as idades e depois tirar a média.
average = 0 # Uso essa variável para tirar a média.
older_man = 0 # Uso essa variável para achar o homem mais velho.
older_name = '' # Essa variável será para dizer o nome do homem mais velho.
count_woman = 0 # Variável que usarei para contar as mulheres sub-20.
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
    if sex in 'Ff' and years_old < 20:
        count_woman = count_woman + 1
average = count / 4
print(f'A média de idade do grupo é de {average:.1f}')
print(f'O homem mais velho tem {older_man} anos e se chama {older_name}.')
if count_woman == 0:
    print('Não temos mulheres abaixo de 20 anos.')
elif count_woman == 1:
    print('Ao todo temos uma mulher abaixo de 20 anos.')
else:
    print(f'Ao todo são {count_woman} mulheres abaixo de 20 anos.')
