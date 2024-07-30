# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('=' * 40)
print(f'{'LOJA DO INTER':^40}')
print('=' * 40)
total = 0
mais1000 = 0
barato = 0
nomebarato = ''
contador = 0
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))
    total = total + valor
    contador = contador + 1
    if valor > 1000:
        mais1000 = mais1000 + 1
    if contador == 1:
        barato = valor
        nomebarato = produto
    else:
        if valor < barato:
            barato = valor
            nomebarato = produto
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('=' * 40)
print(f'{'FIM DO PROGRAMA':^40}')
print('=' * 40)
print(f'O total da compra foi: R$ {total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${barato:.2f}')