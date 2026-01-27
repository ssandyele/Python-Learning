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

#------------------------------------------------------------------
# Entrada de informações de um dicionário

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa: ')).title().strip()
    estado['sigla']=str(input('Sigla do Estado: ')).upper().strip()
    brasil.append(estado.copy()) # Método próprio da estrutura para copiar dicionários
print(brasil)
#[{'uf': 'Paraná', 'sigla': 'PR'}, {'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Alagoas', 'sigla': 'AL'}]
for e in brasil:
    print (e)
# {'uf': 'Paraná', 'sigla': 'PR'}
# {'uf': 'São Paulo', 'sigla': 'SP'}
# {'uf': 'Alagoas', 'sigla': 'AL'}
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
# O campo uf tem valor Paraná.
# O campo sigla tem valor PR.
# O campo uf tem valor São Paulo.
# O campo sigla tem valor SP.
# O campo uf tem valor Alagoas.
# O campo sigla tem valor AL.
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
# Paraná PR 
# São Paulo SP 
# Alagoas AL 
