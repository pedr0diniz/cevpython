# DESAFIO 072 - Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até
# VINTE.

#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por EXTENSO.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

controle = 'S'
while controle == 'S':
    numero = int(input('Digite um número de 0 a 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('Número inválido. Digite um número de 0 a 20: '))
    print(f'Você digitou o número {numero} ({extenso[numero]}).')
    controle = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while controle not in 'SN':
        controle = str(input('Opção inválida! Continuar? [Sim ou Não]')).strip().upper()

#USAR ISSO COMO BASE PARA A CALCULADORA DE AMANDA, SIMPLIFICAR OS IFS DESSA FORMA