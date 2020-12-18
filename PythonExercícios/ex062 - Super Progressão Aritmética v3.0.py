# DESAFIO 062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
#encerra quando disser que quer mostrar 0 TERMOS.

pa = a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
maistermos = i = 1
itotal = 0 #iterações totais
while i <= 10:
    print('O {}º termo da PA é igual a: {}'.format(i, pa))
    pa += razao
    i += 1 #iterações locais
itotal = 10
i = 0
while maistermos != 0:
    maistermos = int(input('Deseja saber mais termos da PA? Se não, digite 0. Se sim, digite quantos: '))
    while maistermos != 0 and i < maistermos:
        print('O {}º termo da PA é igual a: {}'.format(itotal+1, pa))
        pa += razao
        i += 1
        itotal += 1
    i = 0
print('Programa Encerrado!')