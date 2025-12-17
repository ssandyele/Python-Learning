# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome=input('Digite o nome de uma cidade: ').strip()
print('Esta cidade começa com o nome "Santo"? ',end = ' ')
nome=nome.split()
print('SANTO' in nome[0].upper())