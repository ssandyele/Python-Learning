# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os 
# valores únicos digitados, em ordem crescente.

numeros=[]

while True:
    v=int(input('Digite um valor: '))
    if v in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(v)
        print('Valor adicionado com sucesso...')
    resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp=='N':
        break
print('=-'*25)
numeros.sort()
print(f'Você digitou os valores {numeros}')