# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=' * 40)
print('{: ^40}'.format('GERADOR DE P.A.'))
print('=' * 40)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    contador = contador + 1
print('FIM!')
