def voto(anonasc):
    import datetime #economizando memoria!
    atual = datetime.date.today().year
    idade = atual-anonasc
    print()
    if idade<16:
        return f"Com {idade} anos: NAO VOTA"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"


print(voto(2010))