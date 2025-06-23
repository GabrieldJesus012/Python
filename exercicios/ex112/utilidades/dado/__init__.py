def leiaDinheiro(p):
    while True:
        entrada = input(p).strip().replace(',', '.')
        try:
            valor = float(entrada)
            return valor
        except:
            print(f"ERRO! '{entrada}' é um preço inválido.")


