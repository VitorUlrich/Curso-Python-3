#Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.
# adicionar decímetros, metros, decâmetros, hectômetros e quilômetros.

valor = float(input('Digite a distância em metros: '))
cm = valor * 100
mm = valor * 1000
dm = valor * 10
m = valor * 1
dam = valor / 10
hm = valor / 100
km = valor / 1000
print(f'a distância de {valor} metros, corresponde a: '
      f'{cm:.0f} Centímentros, '
      f' {mm:.0f} Milímetros, '
      f'{dm} Decímetros, '
      f'{m:.0f} Metros, '
      f'{dam} Decâmetros, '
      f'{hm} Hectômetros, '
      f'{km} Quilômetros, ')
