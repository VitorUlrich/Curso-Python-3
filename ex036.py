# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.

valorcasa = float(input('Qual o Valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = valorcasa / (anos * 12)
print(f'Para pagar uma casa de R${valorcasa:.2f} em {anos} anos')
print(f'A prestação será de R${prestação}')
minimo = salario * 30 / 100
if prestação >= minimo:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
