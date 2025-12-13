#Escreva um programa que converta uma temperatura digitando 
# em graus Celsius e converta para graus Fahrenheit.

print("CONVERSOR DE TEMPERATURA")
celsius=float(input("Digite uma temperatura em celsius: "))
fahren=(celsius*1.8)+32
print("A temperatura {}ºC equivale à {}ºF".format(celsius,fahren))
