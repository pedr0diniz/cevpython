from math import ceil

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}.'.format(m))
if m >= 5.95:
    print('Você está aprovado, parabéns!')
else:
    print('Você está reprovado, estude mais na próxima!')

#ou

print('Aprovado!' if m>= 5.95 else 'Reprovado!')