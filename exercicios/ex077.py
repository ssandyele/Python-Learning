# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = (
    'programacao', 'arquitetura', 'calculo', 'logica', 'ciencia', 'estatistica',
    'matematica', 'engenharia', 'extensao', 'redes', 'algoritmos', 'software'
)

for palavra in lista:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')