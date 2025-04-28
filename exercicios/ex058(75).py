numeros = ()
num9=num3=0
pares = ()
for c in range(0,4):
    num = int(input(f"Digite o {c+1}ª número: "))
    numeros += (num,)
    if num == 9:
        num9 +=1
    else:
        num9 +=0
    if num == 3:
        num3 = numeros.index(3)+1
    if num %2==0:
        pares += (num,)
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {num9} vezes')
if num3==0:
    print(f'O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 aparece na {num3} posição')
print("Os valores pares digitados foram ",end="")
for par in pares:
    print(par,end=" ")