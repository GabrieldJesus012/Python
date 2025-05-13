pessoas = []
dados = []
mai=men=0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1]>mai:
            mai = dados[1]
        if dados[1]<men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if resp == "N":
        break
print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f'O maior peso foi de {mai}kg. Peso de ',end="")
for nome,peso in pessoas:
    if peso==mai:
        print(nome,end=" ")
print()
print(f'O menor peso foi de {men}kg. Peso de ',end="")
for nome,peso in pessoas:
    if peso==men:
        print(nome,end=" ")



