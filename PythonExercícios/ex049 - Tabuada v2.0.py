# DESAFIO 049 - Refaça o DESAFIO 009, mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando
#um LAÇO FOR.

num = int(input('Digite um número para ver sua tabuada: '))

for i in range(1,11):
    print('{} x {} = {}'.format(num, i, num*i))