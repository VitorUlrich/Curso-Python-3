# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário atual do funcionário: R$ '))
aumento = 0
if salario > 1250:
    aumento = salario + (salario * 0.10)
if salario <= 1250:
    aumento = salario + (salario * 0.15)
print(f'O salário atual de R${salario:.2f} terá um aumento de R${aumento - salario:.2f}, totalizando R${aumento:.2f}')
