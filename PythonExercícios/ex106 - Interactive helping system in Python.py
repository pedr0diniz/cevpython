# DESAFIO 106 - Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
#aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

#Obs: use cores.

c = ('\033[m', #0 - sem cores
     '\033[0;30;41m', #1 - vermelho
     '\033[0;30;42m', #2 - verde
     '\033[0;30;43m', #3 - amarelo
     '\033[0;30;44m', #4 - azul
     '\033[0;30;45m', #5 - roxo
     '\033[7;30m')    #6 - branco

def cabecalho(msg, cor=0):

    """
    -> Imprime o cabeçalho do sistema PyHELP
    :return: não retorna variável.
    """
    print(c[cor], end='')
    print("~" * (len(msg)+4))
    print(f'  {msg}')
    print("~" * (len(msg)+4))
    print(c[0], end='')


def pyhelp():
    while True:
        foub = str(input("Função ou Biblioteca > ")).strip()
        if foub.upper() == 'FIM':
            print(f"{c[1]}{'SISTEMA ENCERRADO!'}{c[0]}")
            break
        else:
            cabecalho(f'Acessando o manual do comando \'{foub}\'', 4)
            print(c[6], end='')
            help(foub)
            print(c[0], end='')

cabecalho('SISTEMA DE AJUDA PyHELP', 2)
pyhelp()