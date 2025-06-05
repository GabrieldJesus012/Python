import random
def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(0,5):
        lista.append(random.randint(0,10))
    print(*lista)

def somaPar(lista):
    par =0
    for c in lista:
        if c%2==0:
            par +=c
    print(f"Somando os pares de {lista}, temos {par}")

numeros = []

sorteia(numeros)
somaPar(numeros)