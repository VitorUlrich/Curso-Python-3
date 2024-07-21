# Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('==' * 27)
print('Vou escolher um número entre 0 e 5. Tente adivinhar...')
print('==' * 27)
computador = randint(0, 5)
usuario = int(input('Qual número eu pensei? '))
print('==' * 27)
print('              PROCESSANDO...')
sleep(1)
print('==' * 27)
print(f'O número que você escolheu foi: {usuario}.')
print(f'O número que eu pensei foi: {computador}.')
print('==' * 27)
if usuario == computador:
    print('PARABÉNS!! VOCÊ ACERTOU!!! ')
    print(f'Nós dois escolhemos o número {computador}.')
else:
#    print(f'Eu pensei no número {computador}, e você no {usuario}.')
    print('Você errou! Tente novamente.')
print('==' * 27)