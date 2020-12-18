from ex115 import cadastro

def suaOpcao():
    print('-' * 40)
    while True:
        try:
            opt = int(input('Sua opção: '))
            if opt in range(1, 4):
                return opt
            else:
                print(f'\033[0;31mDigite um número entre 1 e 3!\033[m')
        except:
            print(f'\033[0;31mDigite um nº inteiro!\033[m')

def tabular(msg):
        print('-' * 40)
        print(f'{msg:^40}')
        print('-' * 40)

def rodarSistema():
    import codecs #preciso do codecs pra não bugar as strings por conta de acentos
    f = codecs.open('bancodedados.txt', 'a+', 'utf-8-sig')
    while True:
        tabular('MENU PRINCIPAL')
        print('1 - Ver pessoas cadastradas \n2 - Cadastrar nova pessoa \n3 - Sair do sistema')
        opcao = suaOpcao()
        if opcao == 1:
            tabular('PESSOAS CADASTRADAS')
            cadastro.verCadastro()
        if opcao == 2:
            tabular('NOVO CADASTRO')
            cadastro.cadastraUsuario(f)
        if opcao == 3:
            tabular('Saindo do sistema... Até logo!')
            break
