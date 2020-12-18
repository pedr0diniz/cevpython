# DESAFIO 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Digite o nome de uma cidade: ')).upper() #tudo maiúsculo pra não ser case sensitive

sp = cidade.split()

print('SANTO' in sp[0])

#ou

cid = cidade.strip() #tire os espaços iniciais
print(cid[:5] == 'SANTO') #compare se o vetor do início até a casa 5 é igual a SANTO