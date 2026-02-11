def aumentar(valor=0, porc=0):
    return valor + valor * porc / 100


def diminuir(valor=0, porc=0):
    return valor - valor * porc / 100


def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor / 2


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
