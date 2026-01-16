# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

valores=[]

for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c==0:
        maior=menor=valores[c]
    else:
        if valores[c]>maior: maior=valores[c]
        if valores[c]<menor: menor=valores[c]
print('=-'*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições', end='')
for pos, v in enumerate(valores):
    if v==maior:
        print(f' {pos}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições', end='')
for pos, v in enumerate(valores):
    if v==menor:
        print(f' {pos}...', end='')
print()