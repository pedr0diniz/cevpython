# DESAFIO 083 - Crie um programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses abertos e fechados na ORDEM CORRETA.

cont1 = cont2 = 0
expressao = str(input('Digite uma expressão matemática: '))
controle = True

for i in range(0, len(expressao)):
    if expressao[i] == '(':
        cont1 += 1
    if expressao[i] == ')':
        cont2 += 1
    if cont2 > cont1:
        print('Expressão matemática inválida!')
        controle = False
        break
if expressao.count('(') == expressao.count(')') and controle is True:
    print('Expressão matemática válida!')