def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except KeyboardInterrupt:
            print("Usuário preferiu não digitar o número")
            return 0
        except (ValueError, TypeError):
            print("ERRO! por favor, digite um número inteiro válido")

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except KeyboardInterrupt:
            print("Usuário preferiu não digitar o número")
            return 0
        except (ValueError, TypeError):
            print("ERRO! por favor, digite um número real válido")

#programa principal
i = leiaInt("Digite um número Inteiro: ")
r = leiaFloat("Digite um número Real: ")
print(f'o valor inteiro digitado foi {i} e o real foi {r}')
