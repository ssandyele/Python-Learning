# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time=list()
jogador=dict()
gols=list()
while True:
    jogador['nome']=str(input('Nome do jogador: ')).strip().title()
    partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range (0, partidas):
        gols.append(int(input(f'\tQuantos gols na partida {c+1}? ')))
    jogador['gols']=gols.copy()
    jogador['total']=sum(gols)
    gols.clear()
    time.append(jogador.copy())
    while True:
        resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp=='N':
        break
print('=-'*30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('--'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
while True:
    print('--'*30)
    resp=int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp==999:
        break
    elif resp>=len(time) or resp<0:
        print(f'ERRO! Não existe jogador com código {resp}!')
        continue
    print(f'-- LEVANTAMENTO DO JOGADOR {time[resp]["nome"]}')
    for j, g in enumerate(time[resp]['gols']):
        print(f'\tNo jogo {j+1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')