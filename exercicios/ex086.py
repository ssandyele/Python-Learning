# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz=[[], [], []]
for l in range(0,3):
    for c in range(0,3):
        mat=int(input(f'Digite o elemento da posição [{l}][{c}]: '))
        matriz[l].append(mat)
print('=-'*25)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
