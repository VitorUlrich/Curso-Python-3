# Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo
# de 1 até 500.

soma = 0
cont = 0
for c in range(3, 501, 3):
    print('.')
    print(c)
    cont = cont + 1
    soma = soma + c
print(f'A Soma de todos os {cont} valores é: {soma}')
