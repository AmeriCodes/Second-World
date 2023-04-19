# Desenvolva uma lógica que leia o peso e a altura de um pessoa calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida


peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))

imc = peso / (altura ** 2)
print(f'Seu IMC foi calculado em {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc < 25:
    print('Você está no PESO IDEAL.')
elif imc < 30:
    print('Você está com SOBRE PESO.')
elif imc < 40:
    print('Você está OBESO, cuide-se!')
else:
    print('Você está com OBESIDADE MORBINA, emagreça.')
