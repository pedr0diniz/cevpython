# DESAFIO 076 - Crie um programa que tenha uma tupla única com NOMES DE PRODUTOS e seus respectivos PREÇOS, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma TABULAR.

produtos = ('Gabinete Aerocool', 190.00, 'Fonte EVGA', 250.00, 'Placa Mãe B350M-E AM4 ASUS', 350.00, 'HD Sata 1TB',
            200.00, 'SSD Samsung 128GB', 180.00, 'Memória RAM 2x8GB HyperX', 600.00, 'Processador AMD Ryzen 2600',
            800.00, 'Placa de Vídeo EVGA GTX 1070', 1700.00)

print('-' * 50)
#entrada = 'LISTAGEM DE PREÇOS'
#print(f'{entrada:^50}') #aparentemente eu preciso que a string esteja numa variável para eu manipulá-la
print(f'{"LISTAGEM DE PREÇOS":^50}') #não preciso de uma string numa variável pra manipular, apenas preciso usar dois tipos diferentes de aspas.
print('-' * 50)
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<40}R$ {produtos[i+1]:>7.2f}')
    #quero imprimir tudo em 50 espaços
    #nome do produto estendido preenchido com pontos, alinhado à esquerda, em até 40 caracteres
    #'R$ ' ocupam 3 espaços
    #guardo os últimos 7 para o valor exclusivamente. alinho à direita, limito para 7 e ponho 2 casas decimais.