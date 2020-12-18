#enquanto verdadeiro:
    #se chão:
        #passo()
    #se buraco:
        #pula()
    #se moeda:
        #pega
    #se troféu
        #pula
        #interrompa
#pega

#traduzindo

#while True:
    #if chão:
        #passo()
    #if buraco:
        #pula()
    #if moeda:
        #pega
    #if troféu:
        #pula
        #break - me tira do laço while.
#pega





cont = 1
while cont <= 10:
    print(cont, end=' ')
    cont += 1
print('Acabou')

while True: #executa pra sempre
    cont += 1
    print(cont, end=' ')  # loop infinito
    if cont == 100:
        break
print('Acabou')

n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
#print('A soma vale {}'.format(soma))

#UTILIZANDO FSTRINGS

print(f'A soma vale {soma}.')

nome = 'José'
idade = 33
salario = 998
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}')
print(f'{nome:-^20}') #variável nome, ocupando 20 caracteres, centralizada (^) e preenchida com '-'
print(f'{nome:-<20}') #variável nome, ocupando 20 caracteres, esquerdizada (<) e preenchida com '-'
print(f'{nome:->20}') #variável nome, ocupando 20 caracteres, endireitada (>) e preenchida com '-'