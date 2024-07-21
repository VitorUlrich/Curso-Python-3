# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoas}º pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'Ao todo tivemos {menor} pessoas menores de idade')
