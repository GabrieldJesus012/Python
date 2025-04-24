ext= ('zero', "um", "dois", "tres",'quatro', "cinco", "seis", 
        "sete",'oito',"nove", "dez", "onze",'doze','treze','quatorze',
        'quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:
    n= int(input("Digite um número entre 0 e 20:"))
    if 0<=n<=20:
        break
    print("Tente Novamente...", end=" ")

extenso = ext[n]
print(f'Você digitou {extenso}')