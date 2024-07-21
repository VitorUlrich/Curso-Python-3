# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print('==' * 25)
print('           Analisando um Triângulo...')
print('==' * 25)
r1 = float(input('Digite o comprimento da Primeira reta: '))
r2 = float(input('Digite o comprimento da Segunda reta: '))
r3 = float(input('Digite o comprimento da Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM FORMAR um Triângulo.')
else:
    print('As retas acima NÃO PODEM FORMAR um Triângulo.')
