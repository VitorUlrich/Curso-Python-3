# Melhore o jogo do DESAFIO 28 onde o computador vai
# “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint


print('=' * 40)
print('{: ^40}'.format(' JOGO DA ADIVINHAÇÃO! '))
print('=' * 40)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
computador = randint(0,10)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez: ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez: ')
print(f'Acertou!!! foram {palpites} tentativas!')