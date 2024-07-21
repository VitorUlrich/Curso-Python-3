# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 40)
print('{: ^40}'.format(' 10 TERMOS DE UMA P.A. '))
print('=' * 40)

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('=' * 60)
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('FIM')
print('=' * 60)
