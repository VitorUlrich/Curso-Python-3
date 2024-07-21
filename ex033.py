# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

print('Escolha 3 números... ')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

menor = n1
if n2 < n1 and n3 > n2:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor escolhido foi: {menor}')

maior = n1
if n2 > n1 and n3 < n2:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor escolhido foi: {maior}')
