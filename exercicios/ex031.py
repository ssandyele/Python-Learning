# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de 
# até 200Km e R$0,45 parta viagens mais longas.

dist=float(input('Qual a distância da viagem em Km? '))
if dist<=200:
    passagem=0.5*dist
else:
    passagem=0.45*dist
print('O preço da passagem para sua viagem de {:.1f}Km é R${:.2f}'.format(dist,passagem))
