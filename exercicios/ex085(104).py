def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except:
            print("ERRO! Digite um número inteiro válido")
#programa principal
n = leiaInt("Digite um número: ")
print(f'Você acabou de digitar o número {n}')
