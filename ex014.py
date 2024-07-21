# Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

cels = float(input('Digite a temperatura em graus ºC: '))
fahr = ((cels * 9) / 5) + 32
print(f'A temperatura atual de {cels}ºC, corresponde a {fahr}ºF')
