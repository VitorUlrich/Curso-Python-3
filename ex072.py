# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.

numeros = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
continuar = ''
while True:
    escolha = int(input('Escolha um número de 0 a 20: '))
    if 0 <= escolha <= 20:
        print(f'Você digitou o número {numeros[escolha]}')
    else:
        print('Número inválido...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'N':
        break
print('FIM DO PROGRAMA')
