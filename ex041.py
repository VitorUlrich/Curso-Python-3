# A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria,
# conforme a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

nome = str(input('Qual o nome do atleta? '))
nascimento = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nascimento
print(f'O atleta {nome} completa {idade} anos em {atual}.')
if atual - nascimento <= 9:
    print('Categoria: MIRIM')
elif atual - nascimento > 9 and atual - nascimento <= 14:
    print('Categoria: INFANTIL')
elif atual - nascimento > 14 and atual - nascimento <= 19:
    print('Categoria: JÚNIOR')
elif atual - nascimento > 19 and atual - nascimento <= 25:
    print('Categoria: SÊNIOR')
elif atual - nascimento > 25:
    print('Categoria: MASTER')
