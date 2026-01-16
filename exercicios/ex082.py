# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros=[]
pares=[]
impares=[]

while True:
    numeros.append(int(input('Digite um valor: ')))
    resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp=='N':
        break
print('=-'*25)
print(f'A lista completa é {numeros}')
for n in numeros:
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')