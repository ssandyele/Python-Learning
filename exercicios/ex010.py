#Crie um programa que leia quanto dinheiro uma pessoa tem na
#carteira e mostre quantos dólares ela pode comprar
#CONSIDERE US$1,00 = R$3,27

v=float(input('Quantos reais você tem?\n R$'))
d=v/3.27
print('Você pode comprar US${:.2f}'.format(d))

