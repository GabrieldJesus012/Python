import random
from time import sleep
lista = []
jogos = []
print("-"*30, "Joga na Mega Sena".center(30), "-"*30)
qjogos = int (input("Quantos jogos você quer que eu sorteie? "))
tot = 1
while tot <= qjogos:
    cont = 0
    while True:
        num =random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print("-="*5, f" SORTEANDO {qjogos} JOGOS ", "-="*5)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)


