#Escreva um programa que pergunte a quantidade de Km percorridos por um 
#carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmp=float(input('Informe a quantidade de quilômetros percorridos: '))
da=int(input('Por quantos dias o carro foi alugado? '))
preco=(60*da)+(0.15*kmp)
print('Você percorreu {}km em {} dias. Você deve pagar R${:.2f} pelo aluguel do carro!'.format(kmp,da,preco))
