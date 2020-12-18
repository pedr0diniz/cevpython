# DESAFIO 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.

#Para os inferiores ou iguais, o aumento é de 15%.

salarioi = float(input('Qual é o salário do funcionário? R$'))
if salarioi <= 1250:
    salario = salarioi*1.15
else:
    salario = salarioi*1.1
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salarioi,salario))