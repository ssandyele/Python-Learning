# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pessoas=[0.0, 0.0, 0.0, 0.0, 0.0]
for i in range(0,5):
    pessoas[i]=float(input('Digite o peso da pessoa número {} em Kg: '.format(i+1)))
maior=menor=pessoas[0]
for i in range (1,5):
    if pessoas[i]>maior: maior=pessoas[i]
    if pessoas[i]<menor: menor=pessoas[i]
print('Maior peso informado: {:.1f}Kg\nMenor peso informado: {:.1f}Kg'.format(maior,menor))