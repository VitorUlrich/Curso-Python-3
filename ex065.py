# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer
# ou não, continuar a digitar valores.

media = 0
parada = ''
sair = False
contador = 0
maior = 0
menor = 0
total = 0
while not sair:
    if parada in 'S':
        print('=' * 40)
        numeros = int(input('Digite um número: '))
        parada = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        total = total + numeros
        contador = contador + 1
        if contador == 1:
            menor = numeros
            maior = numeros
        else:
            if numeros > maior:
                maior = numeros
            if numeros < menor:
                menor = numeros
    elif parada in 'N':
        print(f'Você digitou {contador} números inteiros')
        print('A média entre todos os números digitados é: {:.2f}'. format(total / contador))
        print(f'O maior valor é {maior} e o menor valor é {menor}')
        print('=' * 40)
        sair = True
    else:
        print('COMANDO INVÁLIDO!')
        parada = str(input('Deseja continuar? [S/N] ')).upper()
        print('=' * 40)
