lista = [[0,0,0],[0,0,0],[0,0,0]]
spar=mai=scol=0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f"Digite um valor: [{l}, {c}]: "))

for l in range(3):
    for c in range(3):
        print(f"{lista[l][c]:^5}", end=" ")
        if lista[l][c] %2 == 0:
            spar +=lista[l][c]
    print()
print(f'A soma dos valores pares é {spar}')
for l in range(3):
    scol +=lista[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(3):
    if c==0:
        mai = lista[1][c]
    elif lista[1][c] >mai:
        mai = lista[1][c]
print(f'O maior valor da segunda linha é {mai}')