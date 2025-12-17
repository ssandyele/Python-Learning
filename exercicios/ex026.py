# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase=input('Digite uma frase: ').upper().strip()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('Ela aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela aparece pela última vez na posição {}'.format(frase.rfind('A')+1))