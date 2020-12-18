# DESAFIO 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e
#CONDIÇÃO DE PAGAMENTO:

#à vista DINHEIRO/CHEQUE: 10% de desconto
#à vista no CARTÃO (1x): 5% de desconto
#em até 2x NO CARTÃO: preço normal
#3x OU MAIS no cartão: 20% de juros

print('=' * 10)
print(' ziniD Store ')
print('=' * 10)

preco = float(input('Digite o preço das compras: R$'))

print('FORMAS DE PAGAMENTO:')
print('[ 1 ] à vista no dinheiro/débito/cheque')
print('[ 2 ] em 1x no cartão')
print('[ 3 ] em 2x no cartão')
print('[ 4 ] em 3x ou mais no cartão')

pag = int(input('Digite a opção de pagamento: '))

if pag == 1 or pag == 2 or pag == 3 or pag == 4:
    print('Sua compra no valor de R${:.2f} saiu por R$'.format(preco), end='')
    if pag == 1:
        preco1 = preco*0.9
        print('{:.2f}.\nVocê teve 10% de desconto, já que você pagou à vista no dinheiro/débito/cheque.'.format(preco1))
    elif pag == 2:
        preco2 = preco*0.95
        print('{:.2f}. \nVocê teve 5% de desconto, já que você pagou em 1x no cartão de crédito.'.format(preco2))
    elif pag == 3:
        print('{:.2f}. \nVocê não teve desconto, já que você pagou em 2x no cartão de crédito.'.format(preco))
    else: #como eu já validei que a opção será 1, 2, 3 ou 4, esse else funciona como pag == 4.
        preco4 = preco*1.2
        print('{:.2f}. \nVocê pagou 20% de juros, já que escolheu pagar 3x ou mais no cartão de crédito.'.format(preco4))
        parcelas = int(input('Informe o número de parcelas: '))
        print('O valor de cada uma das {} parcelas será de R${:.2f}.'.format(parcelas,preco4/parcelas))
else:
    print('Opção inválida!')