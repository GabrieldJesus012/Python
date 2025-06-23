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


def resumo (p=0,taxaaum=10,taxadim=5):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"{'Preço analisado:':<20}{moeda(p):>10}")
    print(f"{'Dobro do Preço:':<20}{dobro(p,True):>10}")
    print(f"{'Metade do Preço:':<20}{metade(p,True):>10}")
    print(f"{f'{taxaaum}% de aumento:':<20}{aumentar(p,taxaaum,True):>10}")
    print(f"{f'{taxadim}% de redução:':<20}{diminuir(p,taxadim,True):>10}")
