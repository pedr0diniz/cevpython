# DESAFIO 096 - Faça um programa que tenha uma função área(), que receba as dimensões de um terreno retangular (LARGURA
#e COMPRIMENTO) e mostre a ÁREA DO TERRENO.

def área(a, b):
    print(f"A área de um terreno de {a}m x {b}m é de {a*b}m².")

print('Controle de Terrenos')
print('--------------------')
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
área(l, c)