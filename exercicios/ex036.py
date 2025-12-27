# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa=float(input('Qual o valor da casa? R$'))
salario=float(input('Qual o salário do comprador? R$'))
duracao=int(input('Em quantos anos o comprador pagará a casa? '))
prestacao=casa / (duracao*12)
print('='*40)
if prestacao > (salario*30/100):
    print('A prestação mensal excedeu 30% do seu salário.')
    print('Salário: R${:.2f}'.format(salario))
    print('30% do salário: R${:.2f}'.format(salario*30/100))
    print('Valor da prestação mensal: R${:.2f}'.format(prestacao))
    print('Por esse motivo, o empréstimo foi NEGADO!')
else:
    print('Valor da prestação mensal: R${:.2f}'.format(prestacao))
    print('Tudo certo. O empréstimo foi APROVADO!')
print('='*40)
