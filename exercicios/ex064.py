# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números 
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n=soma=cont=0
while n!=999:
    n=int(input('Digite um número inteiro: [999 para parar]: '))
    if n==999: break
    soma += n
    cont +=1
print('=-'*26)
print('Você digitou {} número(s) inteiro(s) até digitar 999'.format(cont))
print('A soma entre eles é {}'.format(soma))
print('=-'*26)

