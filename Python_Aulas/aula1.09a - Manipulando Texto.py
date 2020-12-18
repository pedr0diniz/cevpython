#frases = strings = cadeiras de caracteres

frase = 'Curso em Vídeo Python' #minha frase é um vetor string, com cada letra sendo um elemento do vetor
                                #vetores em python começam em 0

i = 0
for i in range(0,len(frase)):
    print('#{} - {}'.format(i,frase[i]))
    i + 1

print()

#Operações com Strings

# -Fatiamento-

print(frase[9]) # me retorna o elemento [9] do meu vetor string
print(frase[9:13]) #me retorna os elementos [9] ao [12] do meu vetor string, não chegando ao segundo elemento dos []
print(frase[9:21:2]) #me retorna os elementos [9], [11], [13], [15], [17], [19]. O ":2] no final é o passo da operação
                     #nesse caso, retornando os caracteres de 2 em 2
print(frase[:5]) #me retorna os caracteres antes do [5], ou seja, até o [4] ([0, 1, 2, 3, 4])
print(frase[15:]) #me retorna do caractere [15] até o final da string
print(frase[9::3]) #me retorna os elementos [9], [12], [15] e [18], no passo 3, retornando de 3 em 3
print()

# -Análise-

print(len(frase)) #me retorna o comprimento da frase
print(frase.count('o')) #conta a quantidade de caracteres. Nesse caso, 'o's minúsculos.
print(frase.count('o',0,13)) #conta quantos 'o's minúsculos existem no intervalo do caractere [0] ao [12]
print(frase.find('deo')) #me retorna onde no vetor string eu encontro 'deo'
print(frase.find('Android')) #caso uma string não seja encontrada, o valor retornado é -1
print('Curso' in frase) #me diz se há um conjunto específico de caracteres no meu vetor string. Se sim = true, se não = false.
print()

# -Transformação-

print(frase.replace('Python','Android')) #troca o primeiro elemento do replace pelo segundo
print(frase.upper()) #capitaliza todas as letras de uma string
print(frase.lower()) #coloca todas as letras da string em caixa baixa
print(frase.capitalize()) #joga todos os caracteres para minúsculo e só o primeiro caractere fica maiúsculo
print(frase.title()) #capitaliza todas as primeiras letras das palavras
print()

frase2 = '   Aprenda Python  ' #frase com espaços a mais antes e depois, propositalmente

print(frase2)
print(frase2.strip()) #remove automaticamente os espaços inúteis no começo e no fim de uma string
print(frase2.rstrip()) #remove os espaços inúteis no fim da string. r de right
print(frase2.lstrip()) #remove os espaços inúteis no começo da string. l de left
print()

# -Divisão-

print(frase.split()) #separa todas as palavras de uma string e um vetor de strings, cada string com cada palavra

# -Junção-

print('-'.join(frase)) #põe um caractere específico (nesse caso o -) entre todos os elementos de uma string
print('-'.join(frase.split())) #nesse caso, frase vira um vetor com cada um de seus elementos sendo uma palavra, logo, cada palavra será junta com o caractere -