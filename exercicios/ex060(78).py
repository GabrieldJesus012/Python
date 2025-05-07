valores = []
for cont in range (0,5):
    valores.append(int(input(f"Digite um valor para a Posição {cont}:")))
print(f'Você digitou {valores}')
maior = max(valores)
minimo = min(valores)

posmaior = []
posminimo = []
for i in range(len(valores)):
    if valores[i] == maior:
        posmaior.append(i)
    if valores[i] == minimo:
        posminimo.append(i)

print(f' O maior valor digitado foi {maior} nas posições {posmaior}')
print(f' O menor valor digitado foi {minimo} nas posições {posminimo} ')

