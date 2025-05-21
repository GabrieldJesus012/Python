import random
from time import sleep
print("-"*30)
print("Joga na Mega Sena".center(30))
print("-"*30)
qjogos = int (input("Quantos jogos você quer que eu sorteie? "))
jogos = []
contador = 0
print("-="*5, f" SORTEANDO {qjogos} JOGOS ", "-="*5)
while contador<qjogos:
    jogo = []
    while len(jogo) <6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:])
    contador +=1
indice = 1
for jogo in jogos:
    print(f"Jogo {indice}: {jogo}")
    indice += 1