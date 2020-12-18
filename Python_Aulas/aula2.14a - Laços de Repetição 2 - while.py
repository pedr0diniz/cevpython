#while é usado quando não sei o range, mas tenho uma condição que precisa ser alcançada

#enquanto não maçã
    #passo()
#pega()

#traduzindo

#while not maçã:
    #passo()
#pega()






#while pode ser utilizado quando não há padrão entre o passo

#enquanto não maçã
    #se buraco
        #pula()
    #se chão
        #passo()
    #se moeda
        #pega
#pega

#traduzindo

#while not maçã:
    #if chão:
        #passo()
    #if buraco:
        #pula()
    #if moeda:
        #pega
#pega






for c in range(1,10):
    print(c, end=' ')
print('FIM')
print()

c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('FIM')
print()

for c in range(1,5): #pra digitar 4 valores. mas e se eu não souber quantos quero digitar?
    n = int(input('Digite um valor: '))
print('FIM')
print()

par = impar = 0
n = 1
while n != 0: #flag, condição de parada
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('FIM. Você digitou {} números pares e {} números ímpares.'.format(par,impar))
print()

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')
