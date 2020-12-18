# DESAFIO 057 - Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
#peça a digitação novamente até ter um valor correto.

sexo = '-'
while sexo not in 'MmFf':
    sexo = str(input('Digite o sexo de uma pessoa [M/F]: ')).strip().upper()[0] #stripo espaços, jogo pra caixa alta
    if sexo not in 'MmFf':                                                      #e só pego a primeira letra.
        print('Opção inválida! Só existem dois sexos, M ou F.')                 #assim, masc ou fem também são válidos.
print('Sexo {} registrado com sucesso!'.format(sexo.upper()))