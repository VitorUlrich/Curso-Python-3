# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

resposta = ' '
maiores = 0
homens = 0
mulheres = 0
while resposta not in 'N':
    print('=' * 40)
    print(f'{'CADASTRO DE PESSOAS:':^40}')
    print('=' * 40)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
    resposta = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        maiores = maiores + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulheres = mulheres + 1
print('=' * 40)
print(f'{'FIM DO PROGRAMA':^40}')
print('=' * 40)
print(f'Você cadastrou {maiores} pessoas maiores de idade')
print(f'Você cadastrou {homens} homens')
print(f'Você cadastrou {mulheres} mulheres com menos de 20 anos')
print('=' * 40)