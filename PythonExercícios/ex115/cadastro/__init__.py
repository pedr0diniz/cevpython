def verCadastro():
    import codecs #preciso do codecs pra não bugar as strings por conta de acentos
    rfile = codecs.open('bancodedados.txt', 'r+', 'utf-8-sig')
    print(rfile.read())


def cadastraUsuario(file):
    while True:
        nome = str(input('Nome: ')).strip().title()
        if nome == '999':
            return #cancelo a adição de uma nova pessoa dessa forma.
        if ("".join(nome.split())).isalpha(): #se o nome sem espaços só conter letras, tá ok
            break
        else:
            print(f'\033[0;31mERRO! Nome não pode conter caracteres numéricos ou especiais!\033[m')
    while True:
        try:
            idade = int(input('Idade: '))
            if 0 < idade < 116:
                break
            elif idade <= 0:
                print(f'\033[0;31mERRO! Digite uma idade positiva!\033[m')
            else:
                print(f'\033[0;31mA pessoa mais velha do mundo tem 116 anos de idade, e provavelmente não é você!\033[m')
                print(f'\033[0;31mDigite uma idade válida!\033[m')
        except:
            print(f'\033[0;31mValor inválido! Digite uma idade inteira!\033[m')
    file.write(f'\n{nome:<30} {idade} anos')
    file.flush() #preciso do flush pra atualizar o arquivo em tempo real
    print(f'Novo registro de {nome} adicionado.')