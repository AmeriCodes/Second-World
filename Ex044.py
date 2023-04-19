# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista, dinheiro / cheque: 10% de desconto
# À vista no cartão : 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('========== COUT-STORE ===========')

price = float(input('Digite o valor da compra R$: '))
payment_method = int(input("""
FORMAS DE PAGAMENTO

[ 1 ] = À vista dinheito / Cheque
[ 2 ] = À vista no cartão
[ 3 ] = 2x no cartão
[ 4 ] = 3x ou mais vezes no cartão

Digite a forma de pagamento: """))

if payment_method == 1:
    final_price = price - (price * 10 / 100)
    print(f'Sua compra de R${price:.2f} receberá um desconto de 10% e ficará por R${final_price:.2f}')
elif payment_method == 2:
    final_price = price - (price * 5 / 100)
    print(f'Sua compra de R${price:.2f} receberá um desconto de 5% e ficará por R${final_price:.2f}')
elif payment_method == 3:
    print(f'Sua compra sairá por 2x de R${price / 2:.2f} SEM JUROS\nO total da sua compra será de R${price:.2f}')
elif payment_method == 4:
    final_price = price + (price * 20 / 100)
    total_installment = int(input('Quantas parcelas: '))
    installment = final_price / total_installment
    print(f'Sua compra será parcelada em {total_installment}x de R${installment:.2f}')
    print(f'Sua compra terá 20% de juros, ficando com um total de {final_price:.2f}')
else:
    print('OPÇÃO DE PAGAMENTO INVÁLIDA, TENTE NOVAMENTE.')
