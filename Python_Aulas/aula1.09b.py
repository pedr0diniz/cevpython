frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase[::-1]) #mostra a frase de trás pra frente

print()

print('Oi')

print("""
três aspas servem para imprimir grandes volumes 
de texto sem dividir ele em vários prints pra 
sair quebrando as linhas""")

print()

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O')) #primeiro capitaliza e depois conta
print(len(frase))
frase2 = '   Curso em Vídeo Python   '
print(len(frase2))
print(len(frase2.strip())) #primeiro stripa e depois retorna o comprimento
print()


frase.replace('Python', 'Android') #strings são imutáveis, prova abaixo
print(frase)
frase = frase.replace('Python', 'Android') #usando atribuições na variável eu consigo mudar
print(frase)
frase = 'Curso em Vídeo Python'
print()

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('video')) #linguagem case-sensitive e que diferencia acentos
print(frase.lower().find('vídeo')) #descapitaliza as maiúsculas primeiro e depois encontra
dividido = (frase.split())
print(dividido)
print(dividido[0])
print(dividido[2] [3]) #na segunda palavra, mostra a letra na casa [3]