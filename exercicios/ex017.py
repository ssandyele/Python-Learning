# Faça um programa que leia o comprimento do cateto oposto e 
# do cateto adjacente de um triângulo retângulo. Calcule e 
# mostre o comprimento da hipotenusa.

import math
co=float(input('Qual o comprimento do cateto oposto? '))
ca=float(input('Qual o comprimento do cateto adjacente? '))
#hip=math.sqrt(co*co+ca*ca)
hip=math.hypot(co,ca)
print('O comprimento da hipotenusa é igual a {:.2f}'.format(hip))
