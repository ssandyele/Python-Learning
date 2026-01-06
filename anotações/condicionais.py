#IF/ELIF/ELSE -----------------------------------------------------


#ESTRUTURA CONDICIONAL SIMPLES (apenas if)
nome=input('Qual seu nome? ').strip().title()
if nome == 'Maria':
    print('Seu nome é bem comum!')
print('Prazer em te conhecer {}!'.format(nome))


#ESTRUTURA CONDICIONAL COMPOSTA (if/else)
idade=int(input('Quantos anos você tem? '))
if idade>=18:
    print('Você já é maior de idade.')
else:
    print('Você ainda não atingiu a maioridade.')

#EXPRESSÃO TERNÁRIA
status = "Maior de idade" if idade >= 18 else "Menor de idade"