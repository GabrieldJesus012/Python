valores = []
for cont in range (0,5):
    valores.append(int(input(f"Digite um valor para a Posição {cont}:")))
print(f'Você digitou {valores}')
maior = max(valores)
minimo = min(valores)
print(f' O maior valor digitado foi {maior} nas posições ', end ="")
for i, v in enumerate(valores):
    if valores[i]==maior:
        print(f"{i}...",end="")
print()
print(f' O menor valor digitado foi {minimo} nas posições ', end ="")
for i,v in enumerate(valores):
    if valores[i] == minimo:
        print(f'{i}...',end="")


