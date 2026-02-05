# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o 
# manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

cores = {'limpa':'\033[m',
         'azul': '\033[7;34m',
         'amarelo':'\033[7;33m',
         'pretoebranco':'\033[7;38m',
         'vermelho':'\033[7;31m',}


def escreva(cor, txt):
    tam=len(txt)+4
    print(cores[cor], end='')
    print('-'*tam)
    print(f'{txt:^{tam}}')
    print('-'*tam)
    print(cores['limpa'],end='')

while True:
    escreva('amarelo', 'SISTEMA DE AJUDA PyHELP')
    comando=str(input('Função ou biblioteca > ')).strip().lower()
    if comando=='fim':
        escreva('vermelho', 'ATÉ LOGO!')
        break
    else:
        escreva("azul", f"Acessando o manual do comando '{comando}'")
        print(cores['pretoebranco'])
        help(comando)
        print(cores['limpa'])
