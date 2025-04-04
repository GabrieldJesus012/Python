print("-*-"*30)
print("SUPERMERCADO MAX2k")
print("-*-"*30)
totgasto = totmil= cont = menor= 0
produtobarato = " "
while True:
    produto= str(input("Nome do produto: "))
    preco = float(input("Preço: R$ "))
    cont +=1
    totgasto +=preco
    if preco > 1000:
        totmil +=1
    if cont == 1 or preco<menor:
        menor = preco
        produtobarato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer comprar mais alguma coisa? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print(f"{"FIM DO PROGRAMA":-^40}")
print(f"O total da compra foi de R$ {totgasto:.2f}")
print(f'Existe {totmil} produtos que custam mais de R$1000,00')
print(f'O produto mais barato foi {produtobarato} que custa R$ {menor:.2f}')
