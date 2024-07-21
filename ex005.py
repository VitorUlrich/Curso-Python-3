#Faça um programa que leia um número Inteiro
# e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um numero: '))
print(f'O numero que você digitou é: {num}')
ante = num - 1
suce = num + 1
print(f'Seu antecessor é: {ante}')
print(f'Seu sucessor é: {suce}')
