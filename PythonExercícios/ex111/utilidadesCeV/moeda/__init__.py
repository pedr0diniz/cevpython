def aumentar(p = 0, taxa = 0, form = False):
    r = p*(1+taxa/100)
    if form == False:
        return r
    else:
        return moeda(r)


def diminuir(p = 0, taxa = 0, form = False):
    r = p*(1-taxa/100)
    if form == False:
        return r
    else:
        return moeda(r)


def dobro(p = 0, form = False):
    r = 2*p
    if form == False:
        return r
    else:
        return moeda(r)


def metade(p = 0, form = False):
    r = p/2
    if form == False:
        return r
    else:
        return moeda(r)

def moeda(p = 0, moeda = 'R$'):
    return f"{moeda}{p:.2f}".replace('.', ',') #imprimindo real, mostrando 2 casas decimas e
                                               # trocando os pontos por vírgulas


def resumo(p = 0, aum = 0, dim = 0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado: ":<20}', end=' ')
    print(moeda(p))
    print(f'{"Dobro do preço: ":<20}', end=' ')
    print(dobro(p, True))
    print(f'{"Metade do preço: ":<20}', end=' ')
    print(metade(p, True))
    print(f'{aum}% de aumento: ', end='     ')
    print(aumentar(p, aum, True))
    print(f'{dim}% de redução: ', end='     ')
    print(diminuir(p, dim, True))
    print('-' * 30)