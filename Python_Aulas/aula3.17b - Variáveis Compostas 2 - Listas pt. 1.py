num = [2, 5, 9, 1]
print(num)
num[2] = 3
num.append(7)
num.sort(reverse=True)
print(num)
num.insert(2, 2) #lembrar que o primeiro parâmetro é o espaço e o segundo é o que vai entrar lá
num.remove(2) #remove o primeiro 2
print(num)

for n in num:
      print(f'{n}...', end=' ')
print()
for c, n in enumerate(num):
      print(f'Na posição [{c}] há o número {n}.')


#MUITO BOM PRA LER VÁRIOS NÚMEROS ESSA PORRA
lista = list()
for cont in range(0, 5):
      lista.append(int(input('Digite um valor: ')))

a = [2, 3, 4, 7]
b = a                       #isso cria um vínculo entre as duas listas. alterações em uma alterarão a outra.
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print()

a = [2, 3, 4, 7]
b = a[:]                   #copia os valores uma lista nas mesmas posições em outra lista, sem vinculá-las
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')