# DESAFIO 036 - Escreva um programa para aprovar o empréstimo bancários para a compra de uma casa. O programa vai
#pergunta o VALOR DA CASA, o SALÁRIO do comprados e em QUANTOS ANOS ele vai pagar.

#Calcule o valor da PRESTAÇÃO MENSAL, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
#será negado.

print('-=-' * 20)
print('AVALIADOR DE EMPRÉSTIMOS BANCÁRIOS')
print('-=-' * 20)
casa = float(input('Digite o valor da casa que você pretende comprar: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
prazo = float(input('Digite a quantidade de anos que você pretende levar para pagar a casa: '))
print()


print('O financiamento de uma casa no valor de R${:.2f} em {:.2f} anos resultaria em prestações de R${:.2f}'.format(casa,prazo,(casa/(prazo*12))))

if casa/(prazo*12) >= salario*0.3:
    print('Seu empréstimo foi negado! \n'
          'A parcela de R${:.2f} custaria uma fração muito grande do seu salário de R${:.2f}. \n'
          'Para essa casa, com esse salário e condições de prazo, a prestação máxima que você pode financiar é de R${:.2f}.'.format(casa/(prazo*12),salario,salario*0.3))
else:
    print('Seu empréstimo foi aprovado!')