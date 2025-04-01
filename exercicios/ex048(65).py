cont = s = media= maior = menor= 0

continuar = 'S'  
while continuar == 'S':  
    n = int(input("Digite um número: "))
    s += n  
    cont += 1  # Conta quantos números foram digitados
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()  # Pergunta se quer continuar
    if cont == 1:
        maior = n
        menor = n
    else:
        if n>maior:
            maior= n
        if n<menor:
            menor= n
media = s/cont
print(f"Você digitou {cont} números e a média  foi de {media} o maior foi {maior} e o menor foi {menor}")