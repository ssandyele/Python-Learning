# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o 
# nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma=0
idhomemmaisvelho=0
homemmaisvelho=''
cont=0
h=0

for i in range (1, 5):
    nome=input('Digite o nome da pessoa {}: '.format(i))
    idade=int(input('Digite a idade da pessoa {}: '.format(i)))
    print('Digite:')
    print('1 para Masculino\n2 para Feminino\n3 para outro')
    gen=int(input('Qual o gênero da pessoa {}? '.format(i)))
    soma += idade
    if gen==1:
        h += 1
        if idade>idhomemmaisvelho:
            idhomemmaisvelho=idade
            homemmaisvelho=nome
    if gen==2 and idade<20:
        cont += 1
media=soma/4

print('='*30)
print('Média de idade do grupo informado: {:.0f} anos'.format(media))
if h==0:
    print('Nenhum homem foi cadastrado.')
else:
    print('Nome do homem mais velho: {}'.format(homemmaisvelho))
print('Há {} mulheres com menos de 20 anos no grupo informado.'.format(cont))