#TUPLAS -----------------------------------------------------------

# Podemos declará-las usando () ou não usando nada
# Exemplo: 
nomes = 'Ana', 'João', 'Maria', 'Pedro' #tupla
#         0       1       2        3  
#        -4      -3      -2       -1

print(nomes[1]) #imprime o nome da posição 1
# João
print(nomes[-2]) #imprime o nome da posição -2
# Maria
print(nomes[1:3]) #imprime a tupla da posição 1 ATÉ a 3 
# ('João', 'Maria')
print(nomes) #imprime a tupla
# ('Ana', 'João', 'Maria', 'Pedro')

#Tuplas são IMUTÁVEIS!
# nomes[1]='José' --> não é possível modificar a tupla. ERRO!
#print(nomes[1]) --> continua sendo 'João'



#MODOS DE IMPRIMIR OS ELEMENTOS DA TUPLA --------------------------

#1
for c in nomes:
    print(f'Meu nome é {c}') 
# Meu nome é Ana
# Meu nome é João
# Meu nome é Maria
# Meu nome é Pedro

#2
tamanho=len(nomes)
for i in range (0, tamanho):
    print(f'Meu nome é {nomes[i]} e sou o número {i} da lista.')
# Meu nome é Ana e sou o número 0 da lista.
# Meu nome é João e sou o número 1 da lista.
# Meu nome é Maria e sou o número 2 da lista.
# Meu nome é Pedro e sou o número 3 da lista.

#3
for pos, n in enumerate (nomes):
    print(f'Eu me chamo {n} e sou o número {pos}.')
# Eu me chamo Ana e sou o número 0.
# Eu me chamo João e sou o número 1.
# Eu me chamo Maria e sou o número 2.
# Eu me chamo Pedro e sou o número 3.

# -----------------------------------------------------------------

print(sorted(nomes)) #coloca os nomes em ordem alfabética
# ['Ana', 'João', 'Maria', 'Pedro']

del(nomes) #deleta a tupla
# print(nomes) #ERRO! name 'nomes' is not defined

#Usando parênteses:
a = (1, 2, 3) #tupla A
b = (4, 5, 6, 7) #tupla B
c = a + b 
d = b + a 

print(c)
# (1, 2, 3, 4, 5, 6, 7)
print(d)
# (4, 5, 6, 7, 1, 2 ,3)

print(c.count(3)) # conta quantas vezes o número '3' aparece na tupla C
# 1
print(c.count(9)) #conta quantas vezes o número '9' aparece na tupla C 
# 0

print(d.index(2)) #mostra em qual posição o número '2' aparece pela primeira vez na tupla D
# 5
#print(d.index(8)) #ERRO! print(d.index(8)) ValueError: tuple.index(x): x not in tuple
