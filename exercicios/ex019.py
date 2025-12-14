#Um professor quer sortear um dos seus quatro alunos para 
# apagar o quadro. Faça um programa que ajude ele, lendo o 
# nome dos alunos e escrevendo na tela o nome do escolhido.

import random
a=input('Digite o nome do primeiro aluno(a): ')
b=input('Digite o nome do segundo aluno(a): ')
c=input('Digite o nome do terceiro aluno(a): ')
d=input('Digite o nome do quarto aluno(a): ')
lista = [a,b,c,d]
print('O aluno escolhido foi: {}'.format(random.choice(lista)))

