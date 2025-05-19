lista = [[0,0,0],[0,0,0],[0,0,0]]
par =soma3=0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f"Digite um valor: [{l}, {c}]: "))
        if lista[l][c] % 2 == 0:
            par+=lista[l][c]
        if c == 2:
            soma3+=lista[l][c]
print("-="*30)
for l in range(3):
    for c in range(3):
        print(f"{lista[l][c]:^5}", end=" ")
    print()
print("-="*30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma3}')
maior2=max(lista[1])
print(f'O maior valor da segunda linha é {maior2}')
