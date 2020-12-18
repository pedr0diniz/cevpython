#tupla: variável imutável que guarda vários valores

#lanche: [hamburguer, suco, pizza, pudim]
#lanche[0] = 'hamburguer'
#lanche[1] = 'suco'
#lanche[2] = 'pizza'
#lanche[3] = 'pudim'

#lanche[0:2] = 'hamburguer', 'suco' #faz o 0 ao 2 mas exclui o 2
#lanche[1:] = 'suco', 'pizza', 'pudim' #vai do suco até o final
#lanche[-1] = 'pudim' #último elemento
#len(lanche) = 4 #quantos elementos tem o meu lanche
#for c in lanche:
    #print(c)
#'hamburguer'
#'suco'
#'pizza'
#'pudim'

#strings são listas, outro tipo de variável composta

#tupla = ()
#lista = []
#dicionário = {}


lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')

print(lanche[1]) #na hora de referenciar, sempre colchete
print(lanche[-2]) #vai imprimir o penúltimo elemento da tupla, 'Pizza'
print(lanche[1:3]) #vai imprimir do elemento 1 ao 3 excluindo o 3, 'Suco', 'Pizza'
print(lanche[2:]) #vai imprimir do 2 ao fim, 'Pizza', 'Pudim'
print(lanche[:2]) #vai imprimir do início ao 2 excluindo o 2, 'Hamburger', 'Suco'
print(lanche[-2:]) #vai imprimir do penúltimo elemento ao fim, 'Pizza', 'Pudim'
print(lanche[-3:]) #imprime do antipenúltimo elemento ao fim, 'Suco', 'Pizza', 'Pudim'
print(lanche) #imprime a tupla completa

for c in range(0, len(lanche)): #jeito que já sabíamos
    print(f'Eu vou comer {lanche[c]} na posição {c}!')
print()
for comida in lanche: #jeito mais simples, não me dá a posição
    print(f'Eu vou comer {comida}!')
print()
for pos, comida in enumerate(lanche): #comando novo, para me dar a posição dentro do for
    print(f'Eu vou comer {comida} na posição {pos}!')
print('Comi pra carai...')

#variáveis declaradas dentro do for são incrementadas automaticamente (?)

print(sorted(lanche)) #cria uma lista e coloca a tupla em ordem alfabética
print(lanche)

a = (2, 5, 4)
print(a)
b = (5, 8, 1, 2)
print(b)
c = a + b #a operação de soma com tuplas serve para concatená-las
print(c)
d = b + a
print(d)
print(len(c))
print(c.count(5)) #quantas vezes apareceu 5 em c
print(c.count(4)) #quantas vezes apareceu o 4
print(c.index(8)) #em que posição está o 8
print(c.index(2)) #em qual posição o PRIMEIRO número 2 aparece
print(c.index(5, 1)) #em qual posição aparece o número 5, PARTINDO DA POSIÇÃO 1

#tuplas em python aceitam múltiplos formatos de dados dentro de uma mesma tupla(string, int, float, etc)

#del(variavel) #apaga uma variável