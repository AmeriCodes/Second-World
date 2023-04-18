# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÂO
# - Média 7.0 ou superior: APROVADO

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2

print(f'Sua nota foi {media}')
if media < 5:
    print('Você foi reprovado.')
elif media >= 5 and media <= 6.9: # Essa linha também pode ser escrita assim #* if 7 > media >= 5:
    print('Você esta em recuperação.')
else:
    print('Você esta aprovado!')
    