import datetime
anoatual = datetime.date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input(f"Em que ano a {pess}ª pessoa nasceu? "))
    idade = anoatual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print(f"Ao todo temos {totmaior} pessoas maiores de idade")
print(f"E também temos {totmenor} pessoas menores de idade")