#LISTAS -----------------------------------------------------------

# Podemos declará-las usando []
# Exemplo: 

num = [2, 5, 9, 1]

print(num) 
# [2, 5, 9, 1]
num[2]=3 #isso funciona, pois listas são mutáveis 
print(num)
# [2, 5, 3, 1]
num.append(7) #adiciona o número 7 no final, adicionando mais um índice
print(num)
# [2, 5, 3, 1, 7]

num.sort() #coloca a lista em ordem crescente
print(num)
# [1, 2, 3, 5, 7]
num.sort(reverse=True) #coloca a lista em ordem DEcrescente
print(num)
# [7, 5, 3, 2, 1]

tam=len(num) #função que retorna quantos elementos a lista possui
print(f'Essa lista tem {tam} elementos')

num.insert(2, 0) #na posição 2, adiciona o número 0
print(num)
# [7, 5, 0, 3, 2, 1]

num.pop() #deleta o elemento do último índice
print(num)
# [7, 5, 0, 3, 2]
num.pop(2) #deleta o elemento do índice 2
print(num)
# [7, 5, 3, 2]

num.insert(2, 2) #insere o número 2 no índice 2
print(num)
# [7, 5, 2, 3, 2]

num.remove(7) #remove o elemento 7
print(num)
# [5, 2, 3, 2]
num.remove(2) #remove o número 2 (como ele vai do início ao fim, procurando o 2, ele vai deletar apenas o primeiro que aparecer)
print(num)
# [5, 3, 2]
#num.remove(4) #remove o elemento 4
#print(num)
# retorna um erro, pois não há '4' na lista
if 4 in num: #verifica se o elemento 4 está na lista antes de removê-lo
    num.remove(4)
else:
    print('O número 4 não foi encontrado na lista')


#------------------------------------------------------------------
# Iniciando uma lista vazia
#1
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print(valores)
# [5, 9, 4]

for v in valores:
    print(f'{v}...', end =' ')
# 5... 9... 4... 

print('\n')

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista.')
# Na posição 0, encontrei o valor 5!
# Na posição 1, encontrei o valor 9!
# Na posição 2, encontrei o valor 4!
# Cheguei ao final da lista.

#2
elem = list()
for c in range(0, 5):
    elem.append(int(input('Digite um valor: '))) #preenche uma lista com valores digitados pelo usuário

for pos, e in enumerate(elem):
    print(f'Na posição {pos}, encontrei o valor {e}!')
print('Cheguei ao final da lista.')
#exemplo de saída: 
# Na posição 0, encontrei o valor 5!
# Na posição 1, encontrei o valor 6!
# Na posição 2, encontrei o valor 1!
# Na posição 3, encontrei o valor 8!
# Na posição 4, encontrei o valor 3!
# Cheguei ao final da lista.


#------------------------------------------------------------------
# Cópia e ligação de listas

# ligação: se altero uma, a outra se altera também
a = [2, 3, 4, 7]
b = a #cria uma ligação entre as listas b & a
b[2]=8 #o índice 2 da lista B recebe o elemento '8', mas por conta da ligação, a lista A também é alterada da mesma forma
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Lista A: [2, 3, 8, 7]
# Lista B: [2, 3, 8, 7]

# cópia: apenas faz uma copia de uma lista
c = [3, 5, 7, 9]
d = c[:] # D recebe todos os valores de C (cópia de C dentro de D)
d[2]=0 #altera o elemento do índice 2 da apenas da lista D, pois não há conexão entre C & D
print(f'Lista C: {c}')
print(f'Lista D: {d}')
# Lista C: [3, 5, 7, 9]
# Lista D: [3, 5, 0, 9]

#------------------------------------------------------------------
# LISTAS DE LISTAS / MATRIZ

teste=list() #inícia teste como uma lista vazia
teste.append('Ana') # teste = ['Ana']
teste.append(40) # teste = ['Ana', 40]
galera=list() #inícia galera como uma lista vazia
galera.append(teste[:]) #copia os dados de 'teste' em 'galera'
teste[0]='Maria' # teste = ['Maria', 40]
teste[1]=22 #teste = ['Maria', 22]
galera.append(teste[:]) #adiciona mais uma cópia de 'teste' em 'galera'
print(galera) 
# [['Ana', 40], ['Maria', 22]]


pessoas=[['André', 19], ['Ana', 18], ['Vínicius', 17], ['Vitória', 20]]
#            0      1      0     1        0       1         0       1 
#               0             1               2                3

print(pessoas)
# [['André', 19], ['Ana', 18], ['Vínicius', 17], ['Vitória', 20]]
print(pessoas[0])
# ['André', 19]
print(pessoas[0][1])
# 19
print(pessoas[2][0])
# Vínicius

for p in pessoas:
    print(p) #imprime cada pessoa da lista
# ['André', 19]
# ['Ana', 18]
# ['Vínicius', 17]
# ['Vitória', 20]

for p in pessoas:
    print(p[0]) #imprime apenas os nomes da lista
# André
# Ana
# Vínicius
# Vitória

for p in pessoas: 
    print(p[1]) #imprime apenas as idades da lista
# 19
# 18
# 17
# 20

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
# André tem 19 anos de idade.
# Ana tem 18 anos de idade.
# Vínicius tem 17 anos de idade.
# Vitória tem 20 anos de idade.

ind=list()
dado=list()
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    ind.append(dado[:]) #lista 'ind' recebe uma cópia dos dados de 'dado'
    dado.clear() #remove todos os elementos de 'dado'
print(ind)
# [['Amanda', 20], ['Bruno', 35], ['Carla', 50], ['David', 12], ['Edmara', 85]]

totmai=totmen=0
for i in ind:
    if i[1]>=18:
        print(f'{i[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{i[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maior(es) e {totmen} menor(es) de idade.')
# Amanda é maior de idade.
# Bruno é maior de idade.
# Carla é maior de idade.
# David é menor de idade.
# Edmara é maior de idade.
# Temos 4 maiores e 1 menores de idade.