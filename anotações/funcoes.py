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

#------------------------------------------------------------------
# Interactive Help / Ajuda Interativa

#import datetime

#help(print) -> Mostra como usar a função print.
#help(list) -> Lista todos os métodos disponíveis para uma lista.
#help(datetime) -> Exibe documentação sobre a biblioteca datetime.

# outro modo:
#print(input.__doc__) # Mostra a documentação da função input.

#------------------------------------------------------------------
# docstrings

def funcao(a, b):
    """
    Docstring para funcao
    
    :param a: Descrição
    :param b: Descrição
    """ #usando três aspas logo abaixo do def, um modelo de docstring surge automaticamente; 
    s=a+b # abaixo da docstring, programamos a função.
    # com isso podemos documentar nossa função. Veja um exemplo:

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
        print('FIM!')
# acima, temos a função contador, documentada. 

#help(contador) -> Usando a função help para contador, a docstring será exibida no terminal como um manual.
# 
#------------------------------------------------------------------
# Parâmetros opcionais

# Parâmetros opcionais em Python são definidos na assinatura da função atribuindo um valor 
# padrão a um argumento, tornando-o facultativo durante a chamada. Se o valor não for fornecido, 
# o Python utiliza o padrão estabelecido. Eles aumentam a flexibilidade, permitindo chamadas com ou sem argumentos. 

def somar(a=0, b=0, c=0): #Valor 0 atribuído aos parâmetros a, b, c. Se o valor de algum(s) desse(s) parâmetro não for passado, a função usará o valor padrão (0).
    s = a + b + c
    print(f'A soma vale {s}')

somar(4, 9, 1)
# A soma vale 14
somar(2, 3)
# A soma vale 5
somar(7)
# A soma vale 7
somar()
# A soma vale 0
somar(c=8, a=9)
# A soma vale 17

#------------------------------------------------------------------
# Escopo de variáveis

def teste(y):
    y += 3
    print(f'Valor de x dentro da função: {x}') #Como x foi declarada no escopo global, a função consegue acessar o valor da variável x.
    # Valor de x dentro da função: 5
    print(f'Valor de y dentro da função: {y}')
    # Valor de y dentro da função: 8

x = 5
teste(x)
print(f'Valor de x fora da função: {x}')
# Valor de x fora da função: 5
#print(f'Valor de y fora da função: {y}') -> isso resultará em um erro, pois a variável y foi declarada no escopo da função teste. No escopo global, y não foi declarada.



def teste2(m):
    m += 2 #Esta variável m, não é a mesma do escopo global, deste modo, a variável m do escopo da função se altera, mas a variável m do global, continua com o valor inalterado pela função.
    print(f'Valor de m dentro da função: {m}')
    # Valor de m dentro da função: 6

m = 4
print(f'Valor de m no escopo global, antes da função ser chamada: {m}')
# Valor de m no escopo global, antes da função ser chamada: 4
teste2(m)
print(f'Valor de m no escopo global, depois da função ser chamada: {m}')
# Valor de m no escopo global, depois da função ser chamada: 4



def teste3(z):
    global w #Faz com que a função use a variável w do escopo global e não crie uma nova variável w dentro da função
    w = 1 #Redefine w como 1
    z += 6
    print(f'Valor de w dentro da função: {w}')
    # Valor de w dentro da função: 1
    print(f'Valor de z dentro da função: {z}')
    # Valor de z dentro da função: 13

w = 7
print(f'Valor de w no escopo global, antes da função ser chamada: {w}')
# Valor de w no escopo global, antes da função ser chamada: 7
teste3(w)
print(f'Valor de w no escopo global, depois da função ser chamada (usando global): {w}')
# Valor de w no escopo global, depois da função ser chamada (usando global): 1


#------------------------------------------------------------------
# Retorno de resultados

def somas(s=0, t=0, u=0):
    total = s + t + u
    return total #Retorna o resultado da soma para o programa principal

r1 = somas(3, 2, 5) #Armazena o total na variável r1
r2 = somas(2, 4) #Armazena o total na variável r2
r3 = somas(8) #Armazena o total na variável r3

print(f'Os resultados foram {r1}, {r2} e {r3}')
# Os resultados foram 10, 6 e 8