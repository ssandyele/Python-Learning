# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será um 
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial do número num.
    """
    fat=1
    for x in range(num, 0, -1):
        fat *= x
        if show==True:
            print( x, end=' ')
            if x==1:
                print('=', end=' ')
            else:
                print('x', end=' ')
    return fat


print(fatorial(5, show=True))
help(fatorial)