#Escreva um programa que leia um valor em metros
#e o exiba convertido em centímetros e milímetros.

#Adicione o resto das medidas depois

print("   CONVERSOR DE MEDIDAS   ")
valor=float(input("Digite um valor em metros: "))
cm=valor*100
mm=valor*1000
dm=valor*10
dam=valor/10
hm=valor/100
km=valor/1000
print("Valor convertido em: ")
print("CENTÍMETROS: {}\nMILÍMETROS: {}".format(cm,mm))
print('DECÍMETROS: {}\nDECÂMETROS: {}\nHECTÔMETROS: {}\nQUILÔMETROS: {}'.format(dm,dam,hm,km))




