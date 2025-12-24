# Escreva um programa que pergunte o salário de um funcionário 
# e calcule o valor do seu aumento. Para salários superiores a 
# R$1250,00, calcule um aumento de 10%. Para os inferiores ou 
# iguais, o aumento é de 15%.

sal=float(input('Digite seu salário: R$'))
if sal>1250:
    print('O valor do aumento é R${:.2f}, agora você ganhará R${:.2f}'.format(sal*10/100,sal+(sal*10/100)))
else: 
    print('O valor do aumento é R${:.2f}, agora você ganhará R${:.2f}'.format(sal*15/100,sal+(sal*15/100)))
