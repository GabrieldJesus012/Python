n=1
impar = 0
par = 0
while n != 0:
    n= int(input("Digite um valor: "))
    if n !=0:
        if n % 2 == 0:
            par +=1
        else:
            impar +=1
print("Acabou")
print(f'Ao todo temos {impar} números impares e {par} números pares')