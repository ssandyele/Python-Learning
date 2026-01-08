# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e 
# qual foi o maior e o menor valores lidos. O programa deve 
# perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma=cont=0
resp=''
while resp!='N':
    num=int(input('Digite um número inteiro: '))
    cont += 1
    soma += num
    if cont==1:
        maior=menor=num
    else:
        if num>maior: maior=num
        if num<menor: menor=num
    resp=input('Você gostaria de digitar mais valores? [S/N]? ').strip().upper()[0]
media=soma/cont
print('-'*45)
print('A média dos {} valores digitados foi: {}'.format(cont,media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior,menor))
print('-'*45)


