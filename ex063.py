# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos
# de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('=' * 40)
print('{: ^40}'.format('SEQUÊNCIA DE FIBONACCI'))
print('=' * 40)
num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
contador = 3
while contador <= num:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    contador = contador + 1
print(' -> FIM')
print('=' * 40)