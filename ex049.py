# Refaça o DESAFIO 9, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

vezes = 1
num = int(input('Digite um número para saber a sua tabuada: '))
print('=' * 25)
print('TABUADA DO NÚMERO:', end=' ')
print('{:^2}!!!'.format(num))
print('=' * 25)
for c in range(1, 11):
    print(f'  {num} x {vezes} = {num * vezes}')
    vezes = vezes + 1
