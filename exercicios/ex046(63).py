print("-"*20)
print("Sequência de Fibonacci")
print("-"*20)
termos=int(input("Quantos termos você quer mostrar?"))
cont = 0
anterior = 0
proxima = 1
soma = 0
while cont < termos:
    print(f'{anterior}', end="->")
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
    cont += 1
print('Fim')