#laço com variável de controle

#laço c no intervalo (1,10):
    #dê um passo
#pega

#traduzindo:

#for c in range(1,10):
    #passo()
#pega() #mesmo com o pega fora do laço, ele só será executado depois do laço






#laço c no intervalo (0,3):
    #passo
    #pula #evitando determinados números
#passo
#pega

#traduzindo:

#for c in range(0,3):
    #passo()
    #pula()
#passo()
#pega()






#laço c no intervalo(0,3):
    #se moeda ou maçã
        #pega
    #passo
    #pula
#pega
#passo
#pega

#traduzindo:

#for c in range(0,3):
    #if moeda:
        #pega
    #passo
    #pula
#pega
#passo
#pega






for c in range(1, 6): #ele NÃO CONSIDERA O ÚLTIMO NÚMERO
    print('Oi') #só imprimiu 5x
    print(c)
print('FIM')
print()

for c in range(6, 0, -1): #terceira casa é a iteração
    print(c)
print('FIM')
print()

for c in range(0, 7, 2): #andando de 2 em 2 casas começando do 0
    print(c)
print('FIM')
print()

n = int(input('Digite um número: '))
for c in range(0, n+1): #n+1 pra ele considerar o último número
    print(c)
print('FIM')
print()

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

sum = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    sum += n #sum = sum + n
    if c < 3:
        print('A soma parcial desses números é: {}'.format(sum))
print('A soma final desses números é: {}'.format(sum))