# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() 
# do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(saida):
    cores = {'limpa':'\033[m',
         'vermelho': '\033[31m' }
    while True:
        num=input(saida)
        if num.isnumeric():
            num=int(num)
            break
        print(f'{cores['vermelho']}ERRO! Digite um número inteiro válido.{cores['limpa']}')
    return num
    

n=leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')