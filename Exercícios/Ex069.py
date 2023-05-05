# Crei um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.


men = women = major = women_sub20 = 0 # Mesmo não sendo necessário, eu quis a variável 'women'

while True:
    print('-' * 19)
    print('CADASTRE UMA PESSOA')
    print('-' * 19)
    
    age = int(input('Idade: '))
    if age > 18:
        major += 1
    
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F] ')).strip().upper()[0]
        
    if sex == 'M':
        men += 1
    if sex == 'F':
        women += 1
        if age < 20:
            women_sub20 += 1
                
    question = ' '
    while question not in 'SN':
        print('-' * 19)
        question = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if question == 'N':
        break
    
print(f'Total de pessoas com mais de 18 anos: {major}')
print(f'Ao todo temos {men} homens cadastrados')
print(f'E temos {women_sub20} mulheres com menos de 20 anos.')


# Aqui a baixo vai a resposta do professor ↓
"""
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
"""