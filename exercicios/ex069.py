# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior=homens=mulhervinte=0
cont=1

while True:
    print('=-'*15)
    print(f'---CADASTRE A PESSOA N{cont}---')
    idade=int(input('Digite a idade: '))
    while True:
        gen=input('Gênero: [M/F] ').strip().upper()[0]
        if gen in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    if idade>18:
        maior += 1
    if gen=='M':
        homens += 1
    if gen=='F' and idade <20:
        mulhervinte += 1
    while True:
        resp = input('Você deseja cadastrar mais pessoas? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')    
    if resp=='N':
            break
    cont += 1
print('-'*30)
print('Foram cadastrados:')
print(f'{maior} pessoa(s) com mais de 18 anos')
print(f'{homens} homem(s)')
print(f'{mulhervinte} mulher(es) com menos de 20 anos')
print('-'*30)
