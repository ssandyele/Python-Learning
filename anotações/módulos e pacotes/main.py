#programa principal

import calculos
from uteis import cores, texto

print(cores.c['roxo'])
texto.titulo('CÁLCULOS')
print(cores.c['reset'])

num=int(input("Digite um valor: "))
fat=calculos.fatorial(num)
d=calculos.dobro(num)
t=calculos.triplo(num)
print(f"{cores.c['ft']}O fatorial de {num} é {fat}{cores.c['reset']}")
print(f"{cores.c['db']}O dobro de {num} é {d}{cores.c['reset']}")
print(f"{cores.c['tr']}O triplo de {num} é {t}{cores.c['reset']}")