# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados
# e qual foi a soma entre elas (desconsiderando o flag).
num = 0
contador = 0
soma = 0
while True:
    num = int(input('Digite um número inteiro: [999 para sair] '))
    if num == 999:
        break
    contador = contador + 1
    soma = soma + num
print(f'Você digitou {contador} números')
print(f'A soma de todos eles é igual: {soma}')