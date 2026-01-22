# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cont = 0
dados=[]
temp=[]
while True:
    nome=str(input('Nome: ')).title()
    peso=float(input('Peso: '))
    temp.append(nome)
    temp.append(peso)
    dados.append(temp[:])
    cont += 1
    if cont == 1:
        maior = menor = peso
    else:
        if peso>maior: maior=peso
        if peso<menor: menor=peso
    temp.clear()
    resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Ao todo você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for d in dados:
    if d[1] == maior:
        print(d[0], end=' ')
print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for d in dados:
    if d[1] == menor:
        print(d[0], end=' ')
print()