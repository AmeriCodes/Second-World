# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou o tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

born_year = int(input('Digite ano de nascimento: '))
year = date.today().year

print(f'Quem nasceu em {born_year} tem {year - born_year} anos em {year}.')

enlistment_age = 18
current_age = year - born_year
age_difference = abs(enlistment_age - current_age)

if current_age < enlistment_age:
    print(f'Ainda faltam {age_difference} anos para o seu alistamento.')
    print(f'Seu alistamento será em {year + age_difference}')
elif current_age > enlistment_age:
    print(f'Você já deveria ter se alistado há {age_difference} anos.')
    print(f'Seu alistamento foi em {year - age_difference}')
else:
    print('Você deve se alistar IMEDIATAMENTE!')
