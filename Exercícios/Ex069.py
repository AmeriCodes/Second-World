# Crei um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.


men = women = major = women_sub20 = 0

while True:
    print('-' * 19)
    print('CADASTRE UMA PESSOA')
    print('-' * 19)
    
    age = int(input('Idade: '))
    if age > 18:
        major += 1
    
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F] ')).strip().upper()
        
        if sex == 'M':
            men += 1
        elif sex == 'F':
            women += 1
            if age < 20:
                women_sub20 += 1
                
    question = ' '
    while question not in 'SN':
        print('-' * 19)
        question = str(input('Quer continuar? [S/N] ')).strip().upper()
        
    if question == 'N':
        break
    
print(f'Total de pessoas com mais de 18 anos: 2')
print(f'Ao todo temos {men} homens cadastrados')
print(f'E temos {women_sub20} mulheres com menos de 20 anos.')
