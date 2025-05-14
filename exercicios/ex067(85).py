lista = []
dados = []
for n in range (0,7):
    dados.append(int(input(f"Digite o {n+1}º valor:")))
    lista.append(dados[:])
    dados.clear()
print(f"Os valores digitados foram {lista}")
print (f"Os valores pares digitados foram: ",end="")
for i in range (len (lista)):
    valor = lista[i][0]
    if valor % 2 == 0:
        print(f'{valor}', end=" ")
print()
print (f"Os valores impares digitados foram: ",end="")
for i in range (len (lista)):
    valor = lista[i][0]
    if valor %2 == 1:
        print(f"{valor}", end=" ")
