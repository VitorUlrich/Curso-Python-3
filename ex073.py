# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Internacional.

todostimes = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense',
              'Athletico-PR', 'Bragantino', 'Fortaleza', 'Atlético-MG',
              'São Paulo', 'Cruzeiro', 'Internacional', 'Corinthians',
              'Cuiabá', 'Bahia', 'Santos', 'Goiás', 'Vasco da Gama',
              'América-MG', 'Coritiba')
print('=' * 40)
print(f'Lista de times do Brasileirão 2023: {todostimes}')
print('=' * 40)
print(f'Os 5 melhores colocados no Brasileirão 2023: {todostimes[:5]}')
print('=' * 40)
print(f'Os últimos 4 colocados no Brasileirão 2023: {todostimes[-4:]}')
print('=' * 40)
print(f'Lista de times do Brasileirão 2023 em ordem alfabética: {sorted(todostimes)}')
print('=' * 40)
print(f'O Internacional ficou na {todostimes.index('Internacional') + 1}º posição no Brasileirão 2023:')
print('=' * 40)
