n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print(f'o {n1} é maior que {n2}')
elif n1 < n2:
    print(f'o {n2} é maior que {n1}')
else:
    print(f"Não existe valor maior.{n1} é igual a {n2}")