#Códigos ANSI------------------------------------------------------

# \033[ style ; text ; background m
# \033[x;y;z m

#STYLE
# 0 - none
# 1 - bold
# 4 - underline
# 7 - negative

#TEXT
# 30 - white
# 31 - red
# 32 - green
# 33 - yellow
# 34 - blue
# 35 - pink
# 36 - cyan
# 37 - gray

#BACKGROUND
# 40 - white
# 41 - red
# 42 - green
# 43 - yellow
# 44 - blue
# 45 - pink
# 46 - cyan
# 47 - gray

print('\033[31;43;11mOlá, Mundo!\033[m') #negrito,letra vermelha,fundo amarelo
print('\033[45;30;4mSANDYELE\033[m') #sublinhado,letra branca,fundo rosa
print('\033[7;30mPython\033[m') #letra preta e fundo branco por estar invertido

#------------------------------------------------------------------

nome='Ana'
print('Olá! Prazer em te conhecer, {}{}{}!'.format('\033[1;30;42m', nome, '\033[m')) #negrito,letra branca,fundo verde

#------------------------------------------------------------------

cores = {'limpa':'\033[m',
         'azul': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m' }
idade=20
print('Feliz Aniversário! Parabéns pelos seus {}{}{} anos!'.format(cores['amarelo'],idade,cores['limpa']))