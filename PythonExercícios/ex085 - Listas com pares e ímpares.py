# DESAFIO 085 - Crie um programa onde o usuário possa digitar SETE VALORES NUMÉRICOS e cadastre-os em uma LISTA ÚNICA
#que mantenha separados os valores PARES e ÍMPARES. No final, mostre os valores pares e ímpares em ordem CRESCENTE.

numeros = [[], []]               #a exigência era fazer tudo em uma lista só. sabendo que eu teria uma lista e dentro
for i in range(0, 7):            #dela, separaria pares e ímpares, eu já poderia declarar a lista com as 2 sublistas.
    n = int(input(f'Digite o {i+1}º número: '))       #daí pra frente é só preencher as sublistas de acordo com as
    if n % 2 == 0:                                    #condições do exercício.
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-=-' * 20)
print(f'Os números pares são: {sorted(numeros[0])}.')
print(f'Os números ímpares são: {sorted(numeros[1])}.')