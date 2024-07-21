# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vatual = float(input('Qual a velocidade atual do carro? '))
if vatual > 80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    multa = (vatual - 80) * 7
    print(f'Sua multa será de {multa}')
print('Tenha um bom dia! Dirija com segurança!')
