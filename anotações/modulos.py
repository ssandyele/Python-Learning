#MÓDULOS ----------------------------------------------------------

import math #importa o módulo completo 'math'
num = int(input('Digite um número: '))
raiz = math.sqrt(num) #usa a função 'sqrt' que está dentro do módulo 'math'
print('A raiz de {} é {:.2f}'.format(num,raiz))

#------------------------------------------------------------------

from math import sqrt #importa apenas a função 'sqrt' do módulo 'math'
num = int(input('Digite um número: '))
raiz =sqrt(num) #usa a função sqrt importada diretamente
print('A raiz de {} é {:.2f}'.format(num,raiz))

#------------------------------------------------------------------

import random  #importa o módulo completo 'random'
num=random.randint(1,10) #usa a função 'randint' para gerar um número inteiro aleatório de 0 a 10
print(num)
