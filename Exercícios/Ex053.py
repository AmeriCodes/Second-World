# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# *Não consegui fazer esse exercíocio, esta é a resposta do professor

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' # Isso me parece ser analogo a abrir uma variável recebendo zero, em outros exercícios.
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')

# Esse algorítimo abaixo foi a forma que o GPT me responde
# O GPT não chegou a usar laço, simplismente usou uma forma de fatiamento dentro da condicional.
"""
frase = str(input('Digite sua frase: '))
frase = frase.lower().replace(" ","").replace(",","").replace(".","")
if frase == frase[::-1]:
    print('A frase é PALÍNDROMO!')
else:
    print('A frase NÃO é um PALÍNDROMO!')
    """