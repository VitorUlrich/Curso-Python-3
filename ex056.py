# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

contagem = 0

somaidade = 0
media = 0
maioridade = 0
maisvelho = ''
contmulheres = 0

for pessoa in range(1, 5):
    print('=' * 30)
    print('{: ^30}'.format(f' {pessoa}º PESSOA'))
    print('=' * 30)

    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    contagem = contagem + 1

    somaidade = somaidade + idade
    media = somaidade / contagem
    if pessoa == 1 and sexo in 'Mm':
        maioridade = idade
        maisvelho = nome
    if sexo in 'mM' and idade > maioridade:
        maioridade = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulheres = contmulheres + 1

print(f'A média de idade das pessoas é de: {media} anos.')
print(f'O nome do Homem mais velho do grupo é: {maisvelho.upper()}, com {maioridade} anos ')
print(f'Temos {contmulheres} mulheres com menos de 20 anos no grupo')
