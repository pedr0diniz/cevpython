# DESAFIO 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de
#acordo com a tabela abaixo:

#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso ideal
#Entre 25 e 30: Sobrepeso
#Entre 30 e 40: Obesidade
#Acima de 40: Obesidade mórbida

massa = float(input('Digite sua massa em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = massa/altura**2
print('\nPara uma pessoa que pesa {:.1f}kg e tem {:.2f}m de altura, o IMC é de {:.2f}.\nEssa pessoa está '.format(massa,altura,imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO.')
elif imc < 25:
    print('com o PESO IDEAL. Parabéns!')
elif imc < 30:
    print('com SOBREPESO.')
elif imc < 40:
    print('OBESA.')
else:
    print('com OBESIDADE MÓRBIDA.')