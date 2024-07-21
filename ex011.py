# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da sua parede em metros: '))
altura = float(input('Digite a altura da sua parede em metros: '))
area = altura * largura
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura} x {altura} metros')
print(f'A aréa total da sua parede é de {area:.2f}m²')
print(f'Você vai precisar de {tinta:.2f} litro(s) de tinta para pintar a parede.')
