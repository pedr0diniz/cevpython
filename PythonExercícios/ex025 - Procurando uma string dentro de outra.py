# DESAFIO 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite o nome completo de uma pessoa: ')).upper().split() #upper pra eliminar case sensitive, #split pra eliminar os espaços
nj = (''.join(nome)) #join me resguardar de casos em que o cliente digita o nome sem espaços

print('Há Silva no seu nome? {}'.format('SILVA' in nj))
print('Há Silva no seu nome? {}'.format('SILVA' in nome))