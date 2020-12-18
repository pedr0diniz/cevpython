# DESAFIO 079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma LISTA. Caso
# o número já exista lá dentro, ele NÃO SERÁ ADICIONADO. No final, serão exibidos todos os VALORES ÚNICOS digitados, em
#ORDEM CRESCENTE.

numeros = list()
controle = 'S'
while controle == 'S':
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    #numeros.append(int(input('Digite um valor: ')))
    #if numeros[-1] in numeros[:-1]:
        #print('Valor duplicado! Não vou adicionar...')
        #numeros.pop()
    controle = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while controle not in 'SN':
        controle = str(input('Opção inválida. [Sim] ou [Não]? ')).strip().upper()[0]
print('-=-' * 20)
print(f'Você digitou os valores {sorted(numeros)}.')