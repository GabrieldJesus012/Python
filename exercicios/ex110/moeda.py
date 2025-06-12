def aumentar (p=0,taxa=0,ajustar=False):
    res=  p + (p*taxa/100)
    if ajustar == True:
        return (moeda(res))
    else:
        return res


def diminuir(p=0,taxa=0,ajustar=False):
    res= p - (p*taxa/100)
    if ajustar == True:
        return (moeda(res))
    else:
        return res


def metade (p=0,ajustar=False):
    res= p/2
    if ajustar == True:
        return (moeda(res))
    else:
        return res


def dobro (p=0,ajustar=False):
    res = p*2
    if ajustar == True:
        return (moeda(res))
    else:
        return res


def moeda (p=0, moeda = "R$"):
    return f'{moeda}{p:.2f}'.replace('.',",")


def resumo ():
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    