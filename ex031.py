# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de
# até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45

# passagem = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print(f'Sua passagem vai custar R${passagem:.2f}')
