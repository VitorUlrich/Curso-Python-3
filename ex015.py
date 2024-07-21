# Escreva um programa que pergunte a quantidade de km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por km rodado.

kms = float(input('Digite a quantidade de km´s percorridos: '))
dias = int(input('Digite a quantidade de dias alugados: '))
valordias = dias * 60
valorkms = kms * 0.15
total = valordias + valorkms
print(f'O valor por kms percorridos é de: R$ {valorkms:.2f}')
print(f'O valor por dias alugados é de: R$ {valordias:.2f}')
print(f'O valor total do aluguel é: R$ {total:.2f}')
