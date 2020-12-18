dados = list()
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)
print(dados)

pessoas = list()
pessoas.append(dados[0:2]) #incorporei a lista dados dentro de pessoas[0].
                         # sim, uma lista dentro de um espaço de outra lista
pessoas.append(dados[2:4])
pessoas.append(dados[4:6])
print(pessoas) #pessoas[] é uma lista de 3 elementos com os 6 elementos da lista dados[]

#listas compostas funcionam como matrizes

print(pessoas[0][0]) #primeira célula de pessoas, primeiro elemento
print(pessoas[1][1]) #segunda célula de pessoas, segundo elemento
print(pessoas[2][0]) #terceira célula de pessoas, primeiro elemento
print(pessoas[1]) #imprime a primeira célula inteira