print('='*20)
print("GERADOR DE PA")
print('='*20)

n0=int(input("Primeiro Termo:"))
razao= int(input("Razão:"))
termo = n0
cont = 1

while cont<=10:
    print(f'{termo} ->',end="")
    cont +=1
    termo+=razao
print("Fim")
