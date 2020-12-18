n1 = input('Digite um valor: ')
print(type(n1))
n1 = int(n1)
print(type(n1))

n2 = int(input('Digite outro valor: '))
s = n1 + n2
# print('A soma vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
