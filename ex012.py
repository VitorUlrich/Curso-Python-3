# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o valor do produto: R$ '))
novopreço = preço - (preço * 5 / 100)
print(f'O preço do produto é: R${preço:.2f}')
print(f'Considerando os 5% de desconto, o valor do produto ficará: R$ {novopreço}')
