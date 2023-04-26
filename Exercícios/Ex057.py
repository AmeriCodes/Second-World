# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] ###
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0] ###
print(f'Sexo {sexo} resgistrado com sucesso.')

# Esse fatiamento evita que a pessoa digite o sexo por extenso e o programa não reconheça, desse jeito, caso seja digitado 'masculido' o programa jogara para maiusculo e só pegará a primeira letra, funcionando com se tivesse sido digitado só 'M'.