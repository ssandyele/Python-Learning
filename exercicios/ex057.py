# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo=input('Qual seu gênero? Digite M para masculino ou F para feminino. ').upper().strip()
while sexo!='M' and sexo!='F':
    sexo=input('Resposta inválida! Digite M para masculino ou F para feminino.').upper().strip()
sexo= 'Feminino' if sexo=='F' else 'Masculino'
print('Você selecionou o sexo {}'.format(sexo))