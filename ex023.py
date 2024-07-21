# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.

num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10
c = num // 10 % 10
d = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o numero {num}...')
print(f'Unidade: {u}')
print(f'Dezena: {c}')
print(f'Centena: {d}')
print(f'Milhar: {m}')
