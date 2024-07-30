# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=' * 40)
print('{:^40}'.format('JOGO DO PAR OU ÍMPAR '))
print('=' * 40)
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint (0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria = vitoria + 1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria = vitoria + 1
        else:
            print('Você PERDEU!')
            break
    print('=' * 40)
    print('Vamos jogar novamente...')
print('=' * 40)
print('{:^40}'.format('GAME OVER'))
print(f'Você teve {vitoria} vitória(s) consecutiva(s)')
print('=' * 40)