# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores=[]
for c in range(0, 5):
    num=int(input('Digite um valor: '))
    ind=0
    for v in valores:
        if num<v:
            break
        ind += 1
    if ind==len(valores):
        valores.append(num)
        print('Adicionado ao final da lista...')
    else: 
        valores.insert(ind, num)
        print(f'Adicionado na posição {ind} da lista...')
print('=-'*30)
print(f'Os valores digitados em ordem foram {valores}')
