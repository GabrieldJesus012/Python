totmaior = 0
totmenor = 0

for pess in range(1, 6):
    peso = float(input(f"Qual o seu peso {pess}ª pessoa? "))
    if pess == 1:
        totmaior = peso
        totmenor = peso
    else:
        if peso>totmaior:
            totmaior = peso
        if peso<totmenor:
            totmenor = peso
print(f"O peso maior foi de {totmaior:.2f}kg")
print(f"O peso menor foi de {totmenor:.2f}kg")