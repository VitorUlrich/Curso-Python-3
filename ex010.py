# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.

valor = float(input('Quanto dinheiro você tem na carteira? R$ '))
dol = valor / 5
print(f'Com R$ {valor}, você pode comprar U${dol:.2f}')
