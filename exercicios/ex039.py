#Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
ano=int(input('Qual o ano de seu nascimento? '))
idade=datetime.date.today().year-ano
if idade<18:
    alist=datetime.date.today().year+(18-idade)
    print('Você precisará se alistar em {}'.format(alist))
    print('Faltam {} anos para seu alistamento.'.format(18-idade))
elif idade==18:
    print('Você tem 18 anos, está na hora de se alistar ao exército!')
else: 
    alist=datetime.date.today().year-(idade-18)
    print('O ano de seu alistamento foi em {}'.format(alist))
    print('Já se passaram {} anos do prazo de seu alistamento!'.format(idade-18))