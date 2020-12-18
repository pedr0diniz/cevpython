# DESAFIO 101 - Crie um programa que tenha uma FUNÇÃO chamada voto() que vai receber como PARÂMETRO o ANO DE NASCIMENTO de
#uma pessoa, RETORNANDO um valor LITERAL indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(n):
    from datetime import date
    i = date.today().year - n
    if 16 <= i < 18 or i >= 65:
        print('Voto opcional!')
    elif 18 <= i < 65:
        print('Voto obrigatório!')
    else:
        print('Não vota!')

print('--------------------------------')
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)