# DESAFIO 102 - Crie um programa que tenha uma FUNÇÃO fatorial() que receba dois parâmetros: o primeiro número que indique
#o NÚMERO a calcular e o outro chamado show, que será um valor LÓGICO (opcional) indicando se será mostrado ou não na tela
#o processo de cálculo do fatorial.

#A função deve ter documentação exibida pelo comando help()

def fatorial(n = 1, b = False):

    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param b: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """

    f = 1
    while n >= 1:
        f *= n
        if b == True and n != 1:
            print(f'{n} x ',end='')
        if b == True and n == 1:
            print(f'{n} = {f}')
        n -= 1
    if b == False:
        print(f)

fatorial(8, b=True)
help(fatorial)