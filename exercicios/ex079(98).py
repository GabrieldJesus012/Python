import time
def contador (i,f,p):
    print("-="*20)
    if p == 0:
        p = 1  
    print(f"Contagem de {i} até {f} de {abs(p)} em {abs(p)}")
    if i<f:
        p = abs(p)
        for c in range (i,f+1,p):
            print(c,end=" ",flush=True)
            time.sleep(0.5)
        print("FIM")
    else:
        p = -abs(p)  
        for c in range(i, f - 1, p):
            print(c, end=" ", flush=True)
            time.sleep(0.5)
        print("FIM")
#Programa Principal
contador(1,10,1)
contador(10,0,2)
print("-="*20)
print("Agora é sua vez de personalizar a contagem!")
i = int(input("Inicio: "))
f = int(input("Fim:    "))
p = int(input("Passo:  "))
contador (i,f,p)
