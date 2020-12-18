def leiaDinheiro(msg):
    while True:
        p0 = preço = str(input(msg)).strip()
        if preço.count(',') > 0:
            preço = preço.replace(',','.')
        cont = 0
        for c in preço:
            if c in '0123456789' or c == '.':
                cont += 1
        if cont == len(preço) and preço.count('.') <= 1 and preço != '':
            preço = float(preço)
            break
        else:
            print(f'\033[0;31mERRO: "{p0}" é um preço inválido!\033[m')
    return preço