# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.

lista=[]

while True:
    nome=str(input('Nome: ')).title()
    n1=float(input('Nota 1: '))
    n2=float(input('Nota 2: '))
    media=(n1+n2)/2
    lista.append([nome,[n1,n2],media])
    resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-'*25)
print(f'{"Nº":<5}{"NOME":<12}{"MÉDIA":>6}')
print('-'*25)
for n, d in enumerate(lista):
    print(f'{n:<2}   {d[0]:<10}    {d[2]:>4.1f}')
while True:
    print('-'*30)
    esc=int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if esc==999:
        break
    elif esc>=len(lista) or esc<0:
        print('Não existe nenhum aluno cadastrado com esse número. Tente novamente.')
        continue
    print(f'Notas de {lista[esc][0]} são {lista[esc][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
