def texto(text):
    quant= len(text) +4
    print("-"*quant)
    print(text.center(quant))
    print("-"*quant)

def ajuda():
    texto ("SISTEMA DE AJUDA PyHelp") 
    while True:
        qual = str(input("Função ou Biblioteca > "))
        comando = input("Função ou Biblioteca > ").strip()
        if comando.upper() == "FIM":
            texto("ATÉ LOGO!")
            break
        texto(f"Acessando o manual do comando '{comando}'")
        help(comando)

ajuda()
