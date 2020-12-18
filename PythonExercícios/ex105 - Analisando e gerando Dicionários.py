# DESAFIO 105 - Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar
#um dicionário com as seguintes informações:

#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)

#Adicione também as docstrings da função.

def notas(*n, sit = False):

    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: lista com uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    dicio = {}
    dicio['total'] = len(n)
    dicio['maior'] = max(n)
    dicio['menor'] = min(n)
    dicio['media'] = sum(n)/len(n)
    if sit:
        if dicio['media'] >= 7:
            dicio['situação'] = 'BOA'
        elif 5 <= dicio['media'] < 7:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'
    return(dicio)


help(notas)
resp = notas(5.5, 9.5, 10, 6.5, sit = True)
print(resp)