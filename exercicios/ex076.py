# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

msg='LISTAGEM DE PREÇOS'
lista=(
    'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
    'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
    'Mochila', 120.35, 'Canetas', 22.3, 'Livro', 34.9
)

print ('-'*30)
print(f'{msg:^30}')
print ('-'*30)
for i in range(0,len(lista),2):
    print(f'{lista[i]:.<20}R${lista[i+1]:>8.2f}')
print ('-'*30)
