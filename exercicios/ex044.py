# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento: 
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros

preco=float(input('Qual o preço do produto? R$'))
print('Escolha uma das formas de pagamento abaixo:')
print('[ 1 ] para pagar à vista em dinheiro/cheque;')
print('[ 2 ] para pagar à vista no cartão;')
print('[ 3 ] para pagar em até 2x no cartão;')
print('[ 4 ] para pagar em 3x ou mais no cartão.')
opc=int(input('Sua opção: '))
print('=-=-'*17)
if opc==1:
    print('Pagando à vista no dinheiro/cheque, você ganha 10% de desconto!')
    print('Valor à pagar: R${:.2f}'.format(preco-(preco*10/100)))
elif opc==2:
    print('Pagando à vista no cartão, você ganha 5% de desconto!')
    print('Valor à pagar: R${:.2f}'.format(preco-(preco*5/100)))
elif opc==3:
    print('Pagando em até 2x no cartão, você mantém o preço original do produto!')
    print('Serão ao todo 2 parcelas de R${:.2f} cada.'.format(preco/2))
    print('Valor total à pagar: R${:.2f}'.format(preco))
elif opc==4:
    print('Pagando em 3x ou mais no cartão, você terá que pagar 20% de juros!')
    valor=preco+(preco*20/100)
    parc=int(input('Em quantas parcelas você deseja pagar? '))
    vparc=valor/parc
    print('Serão ao todo {} parcelas de R${:.2f} cada.'.format(parc, vparc))
    print('Valor total à pagar: R${:.2f}'.format(valor))
else:
    print('Você digitou uma opção inválida! Tente novamente.')
print('=-=-'*17)
