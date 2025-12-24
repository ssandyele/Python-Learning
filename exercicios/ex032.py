# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime
ano=int(input('Digite o ano que quer analisar ou digite 0 para analisar o ano atual: '))
if ano==0:
    ano=datetime.date.today().year
if ano%400==0 or ano%4==0 and ano%100!=0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
