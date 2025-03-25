s = 0
for c in range (1,7):
    i = int(input(f"Digite o {c}ª Número: "))
    if i%2==0:
        s+=i
print(f'A soma de todos os números pares é {s}')
