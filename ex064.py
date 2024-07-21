# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).
parada = 0
soma = 0
contador = 0
while not parada == 999:
    numeros = int(input('Digite um número inteiro: '))
    parada = numeros
    soma = soma + numeros
    contador = contador + 1
print(f'Você digitou {contador} números inteiros')
print(f'A soma entre todos os números digitados é: {soma - 999}')
