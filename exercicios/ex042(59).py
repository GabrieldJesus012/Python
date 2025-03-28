n1= int(input("Digite o 1ª valor: "))
n2 = int(input("Digite o 2ª valor:"))
escolha = 0
while escolha != 5:
    print("-=-"*20)
    print("[ 1 ] somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Novos Números")
    print("[ 5 ] Sair do programa")
    escolha = int(input("Escolha uma operação: "))
    if escolha == 1:
        soma = n1+n2
        print(f"{n1} + {n2} = {soma}")
    elif escolha == 2:
        mult = n1*n2
        print(f"{n1} * {n2} = {mult}")
    elif escolha==3:
        if n1 < n2:
            print(f'{n2}>{n1}')
        elif n1>n2:
            print(f"{n1}>{n2}")
        else:
            print(f'{n1} = {n2}')
    elif escolha == 4:
        n1 = int(input("Digite o 1ª valor: "))
        n2 = int(input("Digite o 2ª valor:"))
    elif escolha == 5:
        print("Saindo...")
    else:
        print("Opção ínvalida. Tente novamente.")
    print("-=-"*20)
print("Fim")