import random
print("-=-" * 20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=-" * 20)
v=0 
while True:
    computador = random.randint(0, 10)
    njogador = int(input("Diga um valor: "))
    total = njogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = input("Par ou Ímpar? [P/I] ").strip().upper()[0]
    print(f"Você jogou {njogador} e o computador {computador}. O total de {total}",end=" ")
    print("Deu PAR " if total%2 == 0 else "Deu Ímpar")
    if tipo == "P":
        if total %2==0:
            print("Você Venceu!")
            v+=1
        else:
            print("Você Perdeu!")
            break
    elif tipo == "I":
        if total %2==1:
            print("Você Venceu!")
            v+=1
        else:
            print("Você Perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"Gamer Over! você venceu {v} vezes")

