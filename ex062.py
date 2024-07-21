# Melhore o DESAFIO 61, perguntando para o usuário
# se ele quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.

print('=' * 40)
print('{: ^40}'.format('GERADOR DE P.A.'))
print('=' * 40)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos você deseja mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')