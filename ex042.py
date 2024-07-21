# Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('==' * 25)
print('           Analisando um Triângulo...')
print('==' * 25)
r1 = float(input('Digite o comprimento da Primeira reta: '))
r2 = float(input('Digite o comprimento da Segunda reta: '))
r3 = float(input('Digite o comprimento da Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM FORMAR um Triângulo.')
    if r1 == r2 == r3:
        print('Este é um triângulo EQUILÁTERO')
    if r1 != r2 != r3 != r1:
        print('Este é um triângulo ESCALENO')
    else:
        print('Este é um triângulo ISÓSCELES')
else:
    print('As retas acima NÃO PODEM FORMAR um Triângulo.')
