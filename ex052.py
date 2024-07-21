# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi divisível {total} vezes')
if total == 2:
    print('E por isso, ele é um número PRIMO')
else:
    print('E por isso, ele NÃO é um número PRIMO')
    