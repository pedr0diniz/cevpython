#lanche = ('hamburger', 'suco', 'pizza', 'pudim')
#print(lanche[2]) --------- 'pizza'
#lanche[3] = 'picolé' ------- #vai dar erro, tuplas são imutáveis

#se eu fizer uma lista

lanche = ['hamburger', 'suco', 'pizza', 'pudim']
print(lanche[2])
lanche[3] = 'picolé'
print(lanche)
lanche.append('cookie') #adiciona 'cookie' ao fim da lista, no espaço [4]
print(lanche)
lanche.insert(0, 'cachorro quente') #insere 'cachorro quente' na posição [0]. todo o resto é deslocado pra direita
print(lanche)

#MÉTODOS DE REMOÇÃO

del lanche[3] #intuitivo
print(lanche)
lanche = ['cachorro quente', 'hamburger', 'suco', 'pizza', 'picolé', 'cookie']
lanche.pop(3) #normalmente usado pra apagar o último termo, sem receber parâmetro
print(lanche)
lanche = ['cachorro quente', 'hamburger', 'pizza', 'suco', 'pizza',  'picolé', 'cookie']
lanche.remove('pizza') #remove o primeiro elemento 'pizza' da lista
print(lanche)
print('Depois de deletar o conteúdo de um espaço, a lista é refeita e seus outros componentes são automaticamente '
      'deslocados para que não haja espaços sem valores atribuídos.')
print()

valores = list(range(4, 11))
print(valores)
valores2 = [8, 2, 5, 4, 9, 3, 0]
print(valores2)
valores2.sort() #MODIFICA a lista ordenando os valores em ordem crescente
print(valores2)
valores2.sort(reverse=True) #MODIFICA a lista ordenando os valores em ordem decrescente
print(valores2)
print()