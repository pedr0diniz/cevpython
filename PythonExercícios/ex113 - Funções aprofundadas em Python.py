# DESAFIO 113 - Reescreva a função leiaInt() que fizemos no DESAFIO 104, incluindo agora a possibilidade de digitação
#de um número de tipo inválido. Aproveite e crie também a função leiaFloat() com a mesma funcionalidade.

def leiaInt():
    while True:
        try:
            nint = int(input('Digite um Inteiro: '))
        except KeyboardInterrupt: #quebrado
            print('\033[0;31mERRO: por favor, digite alguma coisa. De preferência um número inteiro.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return nint



def leiaFloat():
    while True:
        try:
            nreal = float(input('Digite um Real: '))
        except (TypeError, ValueError):
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt: #quebrado
            print('\033[0;31mERRO: por favor, digite alguma coisa. De preferência um número real.\033[m')
            return 0
        else:
            return nreal

ni = leiaInt()
nr = leiaFloat()
print(f'O valor inteiro digitado foi {ni} e o real foi {nr}')