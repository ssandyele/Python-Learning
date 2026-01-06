#STRINGS ----------------------------------------------------------

print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Integer at ullamcorper dui. Suspendisse congue lacus eu 
erat aliquam ultricies. Nullam ac elementum ligula. Sed 
eu lorem pellentesque, finibus odio at, pretium est. 
Nullam in mauris elementum, consequat sapien at, maximus 
libero. Praesent orci sapien, lobortis eu nulla mattis, 
blandit mattis lectus. Nulla faucibus vitae purus sed imperdiet. ''') 
# usar ''' dentro de um print permite imprimir textos grandes de uma vez só


frase = 'Feliz Natal e Ano Novo'
# F e l i z   N a t a  l     e     A  n  o     N  o  v  o  
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21

print(frase) #imprime a frase normalmente
# Feliz Natal e Ano Novo
print(frase[3]) #imprime apenas o caractere da posição 3
# i
print(frase[3:13]) #imprime os caracteres da posição 3 à 12
# iz Natal e
print(frase[:13]) #imprime desde o início até o caractere 12
# Feliz Natal e
print(frase[13:]) #imprime a partir do caractere 13 (até o final)
#  Ano Novo
print(frase[1:15:2]) #imprime do caractere 1 até o 14, pulando de 2 em 2 caracteres
# ei aa  
print(frase[::2]) #imprime a string inteira, pulando de 2 em 2 caracteres
# FlzNtleAoNv

#frase[0:1:2]
# 0 - onde começa a frase
# 1 - onde termina a frase (-1)
# 2 - de quanto em quanto "pulam" os caracteres


print(len(frase)) #Mostra o tamanho da string 
# 22
print(frase.count('o')) #Conta quantas vezes a letra 'o' aparece na frase
# 3
print(frase.count('o',0,13)) #Conta quantas vezes 'o' aparece do caractere 0 até o 12
# 0
print(frase.find('tal')) #Mostra a posição inicial onde 'tal' começa na string
# 8
print(frase.find('Dia')) #Procura a palavra 'Dia' na string (retorna -1 se não encontrar)
# -1
print('Feliz' in frase) #Verifica se a palavra 'Feliz' existe na frase
# True

#len()  retorna a quantidade total de caracteres da string
#count()  conta quantas vezes um caractere ou texto aparece (pode ter intervalo)
#find()  retorna a posição do texto procurado ou -1 se não encontrar
#in  verifica se um texto existe na string e retorna True ou False



print(frase.replace('Feliz','Ótimo')) #Substitui 'Feliz' por 'Ótimo' na frase e imprime (não altera a string em si)
print(frase) #Feliz Natal e Ano Novo
frase=frase.replace('Feliz', 'Ótimo') #Altera a string, substituindo 'Feliz' por 'Ótimo'
print(frase.upper()) #Frase em maiúsculo
#ÓTIMO NATAL E ANO NOVO
print(frase.lower()) #Frase em minúsculo
#ótimo natal e ano novo
print(frase.capitalize()) #Apenas a primeira letra da frase em maiúscula
#Ótimo natal e ano novo
print(frase.title()) #Primeira letra de cada palavra em maiúscula
#Ótimo Natal E Ano Novo
print(frase.strip()) #Remove espaços em branco do início e do fim da string
print(frase.rstrip()) #Remove espaços em branco apenas do final da string (RIGHT)
print(frase.lstrip()) #Remove espaços em branco apenas do início da string (LEFT)


print(frase.split()) #Divide a string em uma lista de palavras
# ['Ótimo', 'Natal', 'e', 'Ano', 'Novo']
print('-'.join(frase)) #Junta cada caractere da string com '-' entre eles
# Ó-t-i-m-o- -N-a-t-a-l- -e- -A-n-o- -N-o-v-o
frase=frase.split() #Transforma a frase em uma lista de palavras
print('-'.join(frase)) # Junta as palavras da lista usando '-' como separador
#Ótimo-Natal-e-Ano-Novo