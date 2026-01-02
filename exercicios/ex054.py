# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre 
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual=date.today().year
maior=0
menor=0
for i in range (1,8):
    ano=int(input('Digite o ano de nascimento da pessoa número {}: '.format(i)))
    idade=atual-ano
    if idade>=18:
        maior += 1
    else:
        menor += 1
print('Das 7 pessoas, {} já são de maior e {} ainda não atingiram a maioridade.'.format(maior,menor))