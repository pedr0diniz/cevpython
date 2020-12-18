#indentação obrigatória
#Blocos: parte indentadas do código

#if <argumento>:
    #bloco True
#else:
    #bloco False

tempo = int(input('Quantos anos tem seu carro? '))
if tempo<=3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')
print('--FIM--')

#ou

print('Carro novo' if tempo<=3 else 'Carro velho')
print('--FIM--')

#comandos colados na esquerda sempre acontecem. comandos indentados só acontecer mediante a condição.