# APRENDENDO PYTHON
#ESSE ARQUIVO FOI CRIADO PARA MINHAS ANOTAÇÕES
#-----------------------------------------------
#print("Hello, World!")

#print(1+2)
#print('1'+'2')
#print('1+2')

#nome="Sandyele" 
#idade="18"
#print(nome,idade)

#name=input("Qual é o seu nome? ")
#age=input("Qual sua idade? ")
#print(name,age)

#nome=input("Qual seu nome? ")
#print("Olá",nome,"! Prazer em te conhecer!")

#dia=input("Dia - ")
#mes=input("Mês - ")
#ano=input("Ano - ")
#print("Você nasceu em",dia,"de",mes,"de",ano,". Correto?")

#TIPOS PRIMITIVOS -------------------------------------------

#a=int(input("Primeiro número - "))
#b=int(input("Segundo número - "))
#print("A soma é:",a+b)
#s=a+b
#print('A soma entre',a,'e',b,'é igual à',s)
#print('A soma entre {} e {} é igual à {}'.format(a,b,s))

#n1=input('Digite um número: ')
#print(type(n1))
#n2=int(input('Digite um número: '))
#print(type(n2))

#print('='*20)

#n=input('Qual seu nome? ')
#print('Olá {}!'.format(n))
#print('Olá {:20}!'.format(n))
#print("Olá {:>20}!".format(n))
#print("Olá {:<20}!".format(n))
#print('Olá {:^20}!'.format(n))
#print("Olá {:=^20}!".format(n))

#OPERADORES MATEMÁTICOS -------------------------------------------

#n1=int(input('Digite um número: '))
#n2=int(input('Digite mais um número: '))
#s=n1+n2
#m=n1*n2
#d=n1/n2
#di=n1//n2
#r=n1%n2
#p=n1**n2
#print('RESULTADO DA:\n Soma: {}, Multiplicação: {}, Divisão: {:.2f}'.format(s,m,d), end=', ')
#print('Divisão inteira: {}, Resto da divisão: {}, Potenciação: {}'.format(di,r,p))

#MÓDULOS ----------------------------------------------------------

#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é {:.2f}'.format(num,raiz))

#from math import sqrt
#num = int(input('Digite um número: '))
#raiz =sqrt(num)
#print('A raiz de {} é {:.2f}'.format(num,raiz))

#import random
#num=random.randint(1,10)
#print(num)

#STRINGS ----------------------------------------------------------

#print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#Integer at ullamcorper dui. Suspendisse congue lacus eu 
#erat aliquam ultricies. Nullam ac elementum ligula. Sed 
#eu lorem pellentesque, finibus odio at, pretium est. 
#Nullam in mauris elementum, consequat sapien at, maximus 
#libero. Praesent orci sapien, lobortis eu nulla mattis, 
#blandit mattis lectus. Nulla faucibus vitae purus sed imperdiet. ''')


#frase = 'Feliz Natal e Ano Novo'
#print(frase)
#print(frase[3])
#print(frase[3:13])
#print(frase[:13])
#print(frase[13:])
#print(frase[1:15:2])
#print(frase[::2])

#print(len(frase))
#print(frase.count('o'))
#print(frase.count('o',0,13))
#print(frase.find('tal'))
#print(frase.find('Dia'))
#print('Feliz' in frase)

#print(frase.replace('Feliz','Ótimo'))
#print(frase.upper())
#print(frase.lower())
#print(frase.capitalize())
#print(frase.title())
#print(frase.strip())
#print(frase.rstrip())
#print(frase.lstrip())

#print(frase.split())
#print('-'.join(frase))
#frase=frase.split()
#print('-'.join(frase))
