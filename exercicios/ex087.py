# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz=[[], [], []]
par=terc=0
for l in range(0,3):
    for c in range(0,3):
        mat=int(input(f'Digite o elemento da posição [{l}][{c}]: '))
        if mat%2==0:
            par += mat
        if c==2:
            terc += mat
        if l==1:
            if c==0: 
                maior=mat
            else: 
                if mat>maior:
                    maior=mat
        matriz[l].append(mat)
print('=-'*25)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('=-'*25)
print(f'A soma de todos os valores pares digitados é: {par}')
print(f'A soma dos valores da terceira coluna é: {terc}')
print(f'O maior valor da segunda linha é: {maior}')
