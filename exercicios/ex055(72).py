n= int(input("Digite um número entre 0 e 20:"))
ext= ('zero', "um", "dois", "tres",'quatro', "cinco", "seis", "sete",'oito',"nove", "dez", "onze",'doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while n>21 or n<0:
    print("Tente Novamente...")
    n= int(input("Digite um número entre 0 e 20:"))

extenso = ext[n]
print(f'Você digitou {extenso}')