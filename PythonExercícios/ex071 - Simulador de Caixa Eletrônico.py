# DESAFIO 071 - Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO. No início, pergunte ao usuário qual
#será o VALOR A SER SACADO (número inteiro) e o programa vai informar quantas CÉDULAS de cada valor será entregues.

#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

#valor = int(input('Digite o valor que deseja sacar: '))
#c50 = valor // 50
#c20 = (valor - c50*50) // 20
#c10 = (valor - c50*50 - c20*20) // 10
#c1 = valor - c50*50 - c20*20 - c10*10

#c = [c50, c20, c10, c1]
#print(f'Ao sacar R${valor},00, você recebe:')
#for i in range(0,4):                                         #TENTATIVA 2 - VARIÁVEIS DEMAIS, SEM WHILE
 #   if i == 0:
 #       d = 50
 #   if i == 1:
 #       d = 20
 #   if i == 2:
 #       d = 10
 #   if i == 3:
 #       d = 1
 #   if c[i] != 0:
 #       print(f'{c[i]} cédulas de R${d},00.')

#print(f'Ao sacar R${valor},00 você recebe:'                   #TENTATIVA 1 - IMPRIMINDO VALORES COM 0 NOTAS, SEM WHILE
     # f'\n{c50} cédulas de R$50,00;'
     # f'\n{c20} cédulas de R$20,00;'
     # f'\n{c10} cédulas de R$10,00;'
     # f'\n{c1} cédulas de R$1,00.')

ced = 50
cedx = 0
saque = int(input('Digite o valor que você quer sacar: '))
while True:
    if saque >= ced:
        saque -= ced #tiro uma cédula do valor de saque
        cedx += 1 #conto esse cédula
    else:
        if cedx > 0:
            print(f'{cedx} cédulas de R${ced},00.')
        if ced == 50:    #se a cédula era de 50 e o valor do saque é menor do que 50
            ced = 20     #eu mudo pra cédula de 20 e volto pro primeiro if
        elif ced == 20:  #se a cédula era de 20 e o valor do saque é menor do que 20
            ced = 10     #eu mudo pra cédula de 10 e volto pro primeiro if
        elif ced == 10:  #se a cédula era de 10 e o valor do saque é menor do que 10
            ced = 1      #eu mudo pra cédula de 1 e volto pro primeiro if
        cedx = 0         #zero o contador de cédulas depois de cada iteração
        if saque == 0:
            break

