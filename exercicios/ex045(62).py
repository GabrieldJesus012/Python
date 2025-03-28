print('='*20)
print("GERADOR DE PA")
print('='*20)

n0=int(input("Primeiro Termo:"))
razao= int(input("Razão:"))
termo = n0
cont = 1
total = 0
mais = 10
while mais != 0:
    total +=mais
    while cont<=total:
        print(f'{termo} ->',end="")
        cont +=1
        termo+=razao
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais?"))
print(f"Fim, {total} termos mostrados")