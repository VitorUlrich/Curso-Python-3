# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nomecompleto = str(input('Qual o seu nome completo? ')).strip()
lista = nomecompleto.split()
print('Muito prazer em te conhecer!')
print(f'Seu nome completo é: {lista}')
print(f'Seu primeiro nome é: {lista[0].capitalize()}')
print(f'Seu Sobrenome nome é: {lista[len(lista) - 1].capitalize()}')
