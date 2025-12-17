# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome=input('Qual seu nome completo? ').strip()
print('Seu nome em:\n   -Maiúsculo: {}\n   -Minúsculo: {}'.format(nome.upper(),nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
nome=nome.split()
print('Quantidade de letras do primeiro nome ({}): {}'.format(nome[0],len(nome[0])))  
