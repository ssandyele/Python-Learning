# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(ano):
    idade=anoAtual-ano
    if 18 <= idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


anoAtual = date.today().year
nasc=int(input('Em que ano você nasceu? '))
print(voto(nasc))