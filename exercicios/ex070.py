# Crie um programa que leia o nome e o preço de vários produtos. O programa 
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

cont=1
caro=soma=precobarato=0

print('=-=-=- LISTA DE COMPRAS -=-=-=')
while True:
    nome=input('Digite o nome do produto: ').strip().capitalize()
    preco=float(input('Qual o preço do produto? R$'))
    soma += preco
    if preco>1000:
        caro += 1
    if cont==1:
        barato = nome
        precobarato = preco
    else:
        if preco<precobarato:
            barato = nome
            precobarato = preco
    while True:
        resp=input('Deseja cadastrar mais produtos? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp=='N':
        break
    cont +=1
    print('-'*30)
print('-'*30)
print(f'Foram cadastrados {cont} produtos.')
print(f'O total gasto na compra é de R${soma:.2f}.')
print(f'{caro} produto(s) custa(m) mais de R$1000,00.')
print(f'{barato} é o produto mais barato (R${precobarato:.2f}).')
