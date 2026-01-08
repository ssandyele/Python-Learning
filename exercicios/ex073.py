# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Santos.

times = (
    'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense',
    'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Bragantino',
    'Atlético-MG', 'Santos', 'Corinthians', 'Vasco da Gama', 'EC Vitória',
    'Internacional', 'Ceará SC', 'Fortaleza', 'Juventude', 'Sport Recife'
)

print('-'*30)
print(f'LISTA DE TIMES DO BRASILEIRÃO: {times}')
print('-'*30)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-'*30)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-'*30)
print(f'Lista dos 20 primeiros colocados no Brasileirão em ORDEM ALFABÉTICA: {sorted(times)}')
print('-'*30)
print(f'O Santos está na {times.index("Santos")+1}º posição.')