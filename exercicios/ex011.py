#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta 2m².

print('DIGITE AS INFORMAÇÕES EM METROS!')
l=float(input('Qual a largura da parede? '))
a=float(input('Qual a altura da parede? '))
area=a*l
t=area/2
print('A área da parede é igual à {}m²'.format(area))
print('Será necessário {} litros de tinta para pintá-la'.format(t))