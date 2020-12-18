teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
print(teste)
#galera.append(teste) #cria um vínculo entre as estruturas. o que mudar em teste, muda em galera
galera.append(teste[:]) #colocando esse argumento em teste, copio os valores sem vincular as listas
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print()

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2)
print(galera2[0])
print(galera2[0][0])
print(galera2[2][1])
for p in galera2:
    print(p)
print('Só os nomes: ', end='')
for p in galera2:
    print(f'{p[0]}', end=' ')
print('\nSó as idades: ', end='')
for p in galera2:
    print(f'{p[1]}', end=' ')
print()
print()

galera3 = list()
dado = list() #crio uma lista temporária que não guarda valores, só pra leitura
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:]) #adiciono os dados da lista dado[] a uma célula de galera3[]
    dado.clear() #limpo a lista dado[]. se o comando de cima fosse galera3.append(dado), eu vincularia as 2 listas
                 #e o clear limparia as duas listas.
totmai = totmen = 0
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(galera3)
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
