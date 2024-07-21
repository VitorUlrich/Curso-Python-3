# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

oposto = float(input('Digite a medida do cateto oposto: '))
adjacente = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
print(f'A Hipotenusa do triângulo será de {hipotenusa:.2f}')
