# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n=int(input('Digite um número inteiro: '))
print('-- TABUADA DO {} --'.format(n))
for c in range (0, 11):
    print("{} * {:2} = {}".format(n, c, n*c))
print('-'*15)   
