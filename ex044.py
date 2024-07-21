# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros


print('{:=^40}'.format(' LOJA DO INTER '))
produto = float(input('Qual o valor do produto? R$ '))
print('''[ 1 ] à vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço formal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
pagamento = int(input('Qual a condição de pagamento?: '))
if pagamento == 1:
    total = produto - (produto * 10 / 100)
elif pagamento == 2:
    total = produto - (produto * 5 / 100)
elif pagamento == 3:
    total = produto
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')
elif pagamento == 4:
    total = produto + (produto * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com juros')
else:
    total = produto
    print('Opção INVÁLIDA. Tente novamente!')
print(f'Sua compra de R${produto:.2f} irá custar R${total:.2f} no final.')