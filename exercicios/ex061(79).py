valores = []
while True:
    numeros =int(input(f"Digite um valor:"))
    if numeros in valores:
        print("Valor duplicado! Não vou adicionar")
    else:
        valores.append(numeros)
        print("Valor adicionado com sucesso...")
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print('-=-'*20)
valores.sort() 
print(f'Você digitou os valores {valores}')
