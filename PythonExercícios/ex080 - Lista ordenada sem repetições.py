# DESAFIO 080 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma LISTA, já na
#posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = list()
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n >= max(numeros):
        numeros.insert(i, n) #ponho o maior na posição i, #posso usar numeros.append(n) também
        print('Adicionado ao final da lista...')
    elif i != 0 and n <= min(numeros):
        numeros.insert(0, n) #ponho o menor na posição 0
        print('Adicionado na posição 0 da lista...')
    elif i >= 2 and min(numeros) < n < max(numeros): #numeros[0] e #numeros[1] serão os primeiros minimo e maximo
        cont = 0                                     #então limito minha condição pra a partir do i >= 2
        for c in range(0, i):
            if n > numeros[c]:
                cont += 1
        numeros.insert(cont, n)
        print(f'Adicionado na posição {cont} da lista...')
print(numeros)