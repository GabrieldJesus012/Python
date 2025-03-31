n1= int(input("Digite o um número [999 para parar]: "))
d = 0
s = 0
while n1!= 999:
    n1 = int(input("Digite o um número [999 para parar]:"))
    d += 1
    if n1!=999:
        s +=n1
print(f"Você digitou {d} números e a soma entre eles foi de {s}")