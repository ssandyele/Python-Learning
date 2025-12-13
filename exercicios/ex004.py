#Faça um programa que leia algo pelo teclado e mostre na tela 
#o seu tipo primitivo e todas as informações possíveis sobre ele.

var=input('Digite algo: ')
print("O tipo primitivo dessa variável é: {}".format(type(var)))
print("Só tem espaços? {}".format(var.isspace()))
print("É um número? {}".format(var.isnumeric()))
print("É alfabético? {}".format(var.isalpha()))
print("É alfanumérico? {}".format(var.isalnum()))
print("Está em maiúsulas? {}".format(var.isupper()))
print("Está em minúsculas? {}".format(var.islower()))
print("Está capitalizada? {}".format(var.istitle()))
