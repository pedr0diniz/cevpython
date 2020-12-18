# DESAFIO 100 - Faça um programa que tenha uma LISTA e duas FUNÇÕES chamadas sorteia() e somaPar(). A primeira função vai
#sortear 5 NÚMEROS e vai colocá-los dentro da lista e a segunda função vai mostrar a SOMA entre todos os valores PARES
#sorteados pela função anterior.

def sorteia():
    from random import randint
    from time import sleep
    print("Sorteando 5 valores da lista: ", end='')
    lista = []
    for i in range(0, 5):
        lista.append(randint(1, 10))
        sleep(0.4)
        print(f"{lista[i]} ", end='')
    print("... PRONTO!")
    return(lista)
def somaPar(lis):
    s = 0
    for i in lis:
        if i % 2 == 0:
            s += i
    print(f"Somando os valores pares de {lis}, temos {s}. ")


somaPar(sorteia())