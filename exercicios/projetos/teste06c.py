n1 = float(input('Digite sua 01 nota: '))
n2 = float(input('Digite sua 02 nota: '))
m=(n1+n2)/2

if m>=6:
    print(f'Suas notas {n1} e {n2} é {m}! Você esta aprovado!')
else:
    print(f"Suas notas {n1} e {n2} é {m:.2f}! Você esta reprovado!")
