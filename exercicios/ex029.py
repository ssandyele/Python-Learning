# Escreva um programa que leia a velocidade de um carro. Se ele 
# ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

veloc=float(input('Qual a velocidade do carro? '))
multa=(veloc-80)*7
if veloc>80.0:
    print('MULTADO! O carro ultrapassou o limite permitido de 80km/h')
    print('O valor da multa é R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')
