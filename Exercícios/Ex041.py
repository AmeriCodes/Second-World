# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade.
"""
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SÊNIOR
Acima: MASTER
"""
print('=' * 33)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('=' * 33)


from datetime import date
this_year = date.today().year
born_date = int(input('Digite o ano de nascimento do atleta: ')) # pesquisar como limitar esse input ao ano atual. . .
years_old = this_year - born_date

mirim = 'MIRIM'
infantil = 'INFANTIL'
junior = 'JÚNIOR'
senior = 'SÊNIOR'
master = 'MASTER'

print(f'O atleta tem {years_old} anos.')
if years_old <= 9:
    categoria = mirim
elif years_old <= 14:
    categoria = infantil
elif years_old <= 19:
    categoria = junior
elif years_old <= 25:
    categoria = senior
else:
    categoria = master
print(f'Classificação: {categoria}')
