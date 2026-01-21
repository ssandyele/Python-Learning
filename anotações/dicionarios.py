#DICIONÁRIOS ------------------------------------------------------

# Podemos declará-las usando {}
# Exemplo: 

#dados=dict() ou
dados={'nome':'Fernanda',
       'idade': 20}

# Fernanda     20
#  nome      idade

print(dados['nome'])
# Fernanda
print(dados['idade'])
# 20
print(f'A {dados["nome"]} tem {dados["idade"]} anos.')
# A Fernanda tem 20 anos.

dados['sexo']='F' #adiciona mais um índice (sexo) e junto à ele, seu valor (F)
del dados['idade'] #deleta o índice 'idade' e junto, deleta seu valor (20)

print(dados)
#{'nome': 'Fernanda', 'sexo': 'F'}

#------------------------------------------------------------------
# Valores, chaves & itens // Values, keys & items

filme={'título': 'About Time',
       'ano': 2013,
       'gênero': 'Romance'
}

# About Time  2013   Romance
#  título     ano    gênero

print(filme.values())
# dict_values(['About Time', 2013, 'Romance'])
print(filme.keys())
# dict_keys(['título', 'ano', 'gênero'])
print(filme.items())
# dict_items([('título', 'About Time'), ('ano', 2013), ('gênero', 'Romance')])

for k, v in filme.items():
    print(f'O {k} é {v}.')
# O título é About Time.
# O ano é 2013.
# O gênero é Romance.

#------------------------------------------------------------------
#Dicionário dentro de uma lista

brasil = []
estado1 = {'uf': 'Paraná', 'sigla': 'PR'}
estado2 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)

# Paraná    PR     |  Santa Catarina    SC
#   uf     sigla   |        uf         sigla
#       0          |             1

print(estado1)
# {'uf': 'Paraná', 'sigla': 'PR'}
print(estado2)
# {'uf': 'Santa Catarina', 'sigla': 'SC'}
print(brasil)
# [{'uf': 'Paraná', 'sigla': 'PR'}, {'uf': 'Santa Catarina', 'sigla': 'SC'}]
print(brasil[0])
# {'uf': 'Paraná', 'sigla': 'PR'}
print(brasil[1])
# {'uf': 'Santa Catarina', 'sigla': 'SC'}
print(brasil[0]['uf'])
# Paraná
print(brasil[1]['sigla'])
# SC