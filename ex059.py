# Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print('=' * 40)
print('{: ^40}.'.format(' OPERAÇÕES MATEMÁTICAS '))
print('=' * 40)
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
sair = False
while not sair:
    print('=' * 40)
    print(''' [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa''''')
    print('=' * 40)
    escolha = int(input('O que você deseja fazer? '))
    if escolha == 1:
        print('Você escolheu SOMAR os valores: ')
        print(f'{v1} + {v2} = {v1 + v2}')
    elif escolha == 2:
        print('Você escolheu MULTIPLICAR os valores: ')
        print(f'{v1} x {v2} = {v1 * v2}')
    elif escolha == 3:
        print('Você escolheu QUAL O MAIOR entre os valores: ')
        if v1 > v2:
            maior = v1
            menor = v2
            print(f'{maior} é maior que {menor}')
        elif v2 > v1:
            maior = v2
            menor = v1
            print(f'{maior} é maior que {menor}')
        elif v1 == v2:
            print('Não existe um número MAIOR, os dois são iguais.')
    elif escolha == 4:
        print('Você escolheu NOVOS NÚMEROS.')
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Você escolheu SAIR DO PROGRAMA:')
        print('Finalizando...')
        sair = True
    else:
        print('Você escolheu OPÇÃO INVÁLIDA! TENTE NOVAMENTE: ')
    sleep(1)
sleep(2)
print('=' * 40)
print('{: ^40}'.format('Obrigado!! Volte sempre! :)'))
print('=' * 40)