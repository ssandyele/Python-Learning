# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano 
# de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime
anoAtual=datetime.date.today().year
pessoa={}

pessoa['nome']=str(input('Nome: ')).strip().title()
ano=int(input('Ano de nascimento: '))
pessoa['idade']=anoAtual-ano
pessoa['ctps']=int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps']!=0:
    pessoa['contratação']=int(input('Ano de contratação: '))
    pessoa['salario']=float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + pessoa['contratação'] + 35 - anoAtual
print('-=-'*20)
for k, v in pessoa.items():
    print(f'\t- {k} tem o valor {v}')