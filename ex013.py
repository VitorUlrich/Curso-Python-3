# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário atual do funcionário: R$ '))
novosalario = salario + (salario * 15 / 100)
print(f'O salário atual do funcionário é: {salario}')
print(f'O novo salário, considerando o aumento de 15% é: R$ {novosalario}')
