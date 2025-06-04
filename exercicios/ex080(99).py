def maior(*num):
    print("-="*20)
    print("Analisando os valores passados...")
    tot =maior= 0
    for i in num:
        print (i,end=" ")
        tot+=1
    maior = num[0]
    for i in num:
        if i > maior:
            maior = i
    print(f"Foram informados {tot} valores ao todo")
    print(f'O maior valor informado foi {maior}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(0)
