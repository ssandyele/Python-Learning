# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de 
# cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa=dict()
dados=list()
totIdade=0
while True:
    pessoa['nome']=str(input('Nome: ')).title().strip()
    while True:
        pessoa['sexo']=str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade']=int(input('Idade: '))
    totIdade += pessoa['idade']
    dados.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp=='N':
        break
print('=-'*30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
media=totIdade/len(dados)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for p in dados:
    if p['sexo']=='F':
        print(f"{p['nome']}; ", end='')
print('\nD) Lista de pessoas que possuem idade acima da média:')
for p in dados:
    if p['idade']>media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')