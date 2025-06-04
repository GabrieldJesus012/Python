def area (l,c):
    a = l*c
    print(f"a área de um terreno {l}x{c} é de {a}m²")

print("Controle de terrenos")
print("--------------------")
largura= float(input("Largura (m): "))
comprimento= float(input("Comprimento (m): "))
area(largura,comprimento)