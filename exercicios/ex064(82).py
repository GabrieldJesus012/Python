lista=[]
while True:
    lista.append(int(input("Digite um valor: ")))
    resp=" "
    while resp not in "NS":
        resp= str(input("Quer Continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("-=-"*20)
print(f"A lista completa é {lista}")
par = []
impar = []
for numero in lista:
    if numero %2==0:
        par.append(numero)
    else: 
        impar.append(numero)
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
