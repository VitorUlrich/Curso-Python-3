# Crie um algoritmo que leia um número
# e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um numero: '))
print(f'O numero que você digitou é: {num}')
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print(f'O dobro de {num} é: {dobro}')
print(f'o triplo de {num} é: {triplo}')
print(f'A raiz quadrada de {num} é: {raiz:.2f}')