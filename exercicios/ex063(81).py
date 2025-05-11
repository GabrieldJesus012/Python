lista = []
while True:
    lista.append(int(input(f"Digite um valor:")))
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print('-=-'*20)
print(f'Você digitou {len(lista)}º elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem descrecente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não está na lista')




