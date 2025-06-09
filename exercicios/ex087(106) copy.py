def ajuda(com):
    help (com)

def texto(text):
    tam= len(text) +4
    print("~"*tam)
    print(text.center(tam))
    print("~"*tam)

#programa principal
comando = ""
while True:
    texto ("SISTEMA DE AJUDA PyHelp")
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper()=="FIM":
        break
    else:
        ajuda(comando)
texto ("ATÉ LOGO!")