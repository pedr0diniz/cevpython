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