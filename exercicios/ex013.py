#Faça um algoritmo que leia o salário de um funcionário
#e mostre seu novo salário , com 15% de aumento.

sal=float(input('Digite seu salário:\nR$'))
ns=sal+(sal*15/100)
print('O novo salário com 15% de aumento é R${:.2f}'.format(ns))