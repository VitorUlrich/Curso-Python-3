# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

num = 0
while True:
    print('=' * 40)
    num = int(input('Digite um número para saber a sua tabuada: '))
    if num < 0:
        break
    print('=' * 40)
    print(f'Essa é a tabuada do número: {num:^3} !!!')
    for cont in range (1, 11):
        print(f'{num} x {cont} = {num * cont}')
print('Programa encerrado!')
print('Volte sempre.')