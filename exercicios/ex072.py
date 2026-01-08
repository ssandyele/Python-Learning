# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso=(
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

num=int(input('Digite um número inteiro de 0 a 20: '))
while not 0 <= num <= 20:
    num=int(input('ERRO! Digite apenas números inteiros de 0 a 20: '))
print(f'Você digitou o número {extenso[num]}.')
