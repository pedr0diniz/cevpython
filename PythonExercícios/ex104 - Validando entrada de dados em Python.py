# DESAFIO 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do
#Python, só que fazendo a validação para aceitar apenas um valor numérico.

#Ex: n = leiaInt('Digite um n')

def leiaInt(frase):
    ok = False #precisei criar esse boolean. seria ideal poder usar "if num.isnumeric() is False"
    while ok is False:
        num = str(input("Digite um número: "))
        if num.isnumeric():
            num = int(num)
            ok = True
        if ok is False:
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")
    return num

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')