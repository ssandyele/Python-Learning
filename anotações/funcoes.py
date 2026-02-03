#------------------------------------------------------------------
# FUNÇÕES ---------------------------------------------------------


# Supondo que temos um programa que faz a soma de dois números diferentes
# várias vezes. O código é repetido toda vez para cada soma diferente, se 
# tornando extenso e repetitivo.
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

# Para termos um código mais limpo, criamos uma função chamada 'soma()'
# que recebe os dois números como parâmetros. Deste modo, escrevemos o
# código apenas uma vez e conseguimos utilizá-lo para as diversas somas, 
# deixando o código mais compacto e limpo.

def soma(a, b): #define a função com 'def' e recebe 'a' e 'b' como parâmetros.
    s = a + b
    print(s)

   
soma(4, 5) #chama a função 'soma', passando 4 e 5 como parâmetros
soma(8, 9)
soma(2, 1)
#soma (3, 9, 5) ERRO! É preciso passar exatamente a quantidade de parâmetros da função, nem mais, nem menos.

#------------------------------------------------------------------

def divisao(a, b):
    d = a / b
    print(d)

#outro modo de passar os parâmetros:
divisao(a=10, b=2) #(10/2)
divisao(b=10, a=2) #(2/10)
# RESULTADOS:
# 5.0
# 0.2
#divisao(b=2, 8)   ERRO! Se declarar um parâmetro, é necessário declarar todos

#------------------------------------------------------------------
# EMPACOTAMENTO DE PARÂMETROS
# Quando não sabemos a qnt exata de parâmetros 
def contador(*num): #Usamos o * para "desempacotar" as variáveis
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

    
contador(2, 1, 7) # 3 parâmetros
contador(8, 0) # 2 parâmetros
contador(4, 7, 8, 9, 3) # 5 parâmetros
# Recebi os valores (2, 1, 7) e são ao todo 3 números.
# Recebi os valores (8, 0) e são ao todo 2 números.
# Recebi os valores (4, 7, 8, 9, 3) e são ao todo 5 números.

#------------------------------------------------------------------
# Listas são mutáveis
# Ao passar uma lista para uma função,
# a alteração dentro da função afeta a lista original

def dobra(lst):
    # lst recebe a lista passada como parâmetro
    # NÃO é uma cópia, é a mesma lista da variável original
    pos=0
    while pos < len(lst):
        lst[pos] *= 2 # dobra o valor que está nessa posição, isso modifica a lista original
        pos += 1

valores=[3, 7, 5, 9, 4, 2]
dobra(valores)
print(valores)
# [6, 14, 10, 18, 8, 4]