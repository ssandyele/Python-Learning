print("Hello, World!")

print(1+2) #3
print('1'+'2') #12
print('1+2') #1+2

nome="Sandyele" 
idade="18"
print(nome,idade) #Sandyele 18
name=input("Qual é o seu nome? ")
age=input("Qual sua idade? ")
print(name,age)

nome=input("Qual seu nome? ")
print("Olá",nome,"! Prazer em te conhecer!")

dia=input("Dia - ")
mes=input("Mês - ")
ano=input("Ano - ")
print("Você nasceu em",dia,"de",mes,"de",ano,". Correto?")

#TIPOS PRIMITIVOS -------------------------------------------
a=int(input("Primeiro número - "))
b=int(input("Segundo número - "))
print("A soma é:",a+b)
s=a+b
print('A soma entre',a,'e',b,'é igual à',s)
print('A soma entre {} e {} é igual à {}'.format(a,b,s))

n1=input('Digite um número: ')
print(type(n1)) #retorna o tipo da variável (<class 'str'>)
n2=int(input('Digite um número: '))
print(type(n2)) #retorna o tipo da variável (<class 'int'>)

print('='*20) #imprime o '=' 20 vezes

n=input('Qual seu nome? ')
print('Olá {}!'.format(n)) 
# Olá nome!
print('Olá {:20}!'.format(n)) #Reserva 20 espaços para o nome 
#Olá nome                !
print("Olá {:>20}!".format(n)) #Alinha o nome à direita dentro de 20 espaços 
#Olá                 nome!
print("Olá {:<20}!".format(n)) #Alinha o nome à esquerda dentro de 20 espaços 
#Olá nome                !
print('Olá {:^20}!'.format(n)) #Centraliza o nome dentro de 20 espaços 
#Olá         nome        !
print("Olá {:=^20}!".format(n)) #Centraliza o nome em 20 espaços, preenchendo com "=" 
#Olá ========nome========!