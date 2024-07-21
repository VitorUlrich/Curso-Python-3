# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Digite o peso da pessoa: (Kg) '))
altura = float(input('Digite a idade da pessoa: (m) '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
if imc >= 18.5 and imc < 25:
    print('Você está no peso Ideal')
if imc >= 25 and imc < 30:
    print('Você está com Sobrepeso')
if imc >= 30 and imc < 40:
    print('Você está com Obesidade')
if imc >= 40:
    print('Você está com Obesidade Mórbida')