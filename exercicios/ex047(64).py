n1 = cont = s = 0
n1 = int(input("Digite o um número [999 para parar]:"))
while n1!= 999:
    s +=n1
    cont += 1
    n1 = int(input("Digite o um número [999 para parar]:"))
print(f"Você digitou {cont} números e a soma entre eles foi de {s}")