n = s = 0 
while True:
    n=int(input("Digite um número: [999 para acabar]"))
    if n ==999:
        break
    s +=n
print(f"Acabou, a soma vale {s}")