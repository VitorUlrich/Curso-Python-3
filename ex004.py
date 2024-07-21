#Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print(f'A palavra que você digitou é: {algo}')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'É um numero? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')
