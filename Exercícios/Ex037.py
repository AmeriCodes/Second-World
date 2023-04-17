# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para Binário
# - 2 para Octal
# - 3 para Hexadecimal

number = int(input('Digite um número inteiro: '))
print('''Escolha um das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

option = int(input('Sua opção: '))
if option == 1:
    print(f'{number} convertido para BINÁRIO é igual a {bin(number)[2:]}.')
elif option == 2:
    print(f'{number} convertido para OCTAL é igual a {oct(number)[2:]}.')
elif option == 3:
    print(f'{number} convertido para HEXADECIMAL é igua a {hex(number)[2:]}.')
else:
    print('Opção inválida')
