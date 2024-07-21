# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print(f'{num} Convetido para BINARIO é igual a {bin(num)}')
elif escolha == 2:
    print(f'{num} Convertido para OCTAL é igual a {oct(num)}')
elif escolha == 3:
    print(f'{num} Convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('OPÇÃO INVÁLIDA!')
