def linha (tam=42):
    return "-"*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

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

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c =1 
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc = leiaInt("Sua Opção: ")

def cadastro ():
    cabecalho("NOVO CADASTRO")
    while True:
        try:
            nome = input("Nome: ").capitalize().strip()
            if nome == "":
                print("ERRO! Nome não pode ser vazio.")
            else:
                break
        except KeyboardInterrupt:
            print("\nUsuário preferiu não digitar o nome.")
            return 
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except KeyboardInterrupt:
            print("\nUsuário preferiu não digitar a idade.")
            return 
        except (ValueError, TypeError):
            print("ERRO! Por favor, digite uma idade válida.")
    with open("cadastro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome:<30}{idade:>3} anos\n")
    print(f"Registro de {nome} adicionado com sucesso!")
    menu()

def lerCadastro():
    cabecalho("PESSOAS CADASTRADAS")
    try:
        with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Nenhum cadastro encontrado ainda.")
    menu()