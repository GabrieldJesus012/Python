def menu():
    print("-"*50)
    print("MENU PRINCIPAL".center(50))
    print("-"*50)
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova Pessoa")
    print("3 - Sair do Sistema")

def cadastro ():
    print("-"*50)
    print("NOVO CADASTRO".center(50))
    print("-"*50)
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
    print("-" * 50)
    print("PESSOAS CADASTRADAS".center(50))
    print("-" * 50)
    try:
        with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Nenhum cadastro encontrado ainda.")
    menu()

#programa principal
menu()
while True:
    print("-"*50)
    escolha = input("Sua Opção:")
    if escolha == "1":
        lerCadastro()
    elif escolha == "2":
        cadastro()
    elif escolha == "3":
        print("-"*50)
        print("Saindo do Sistema... até logo!")
        print("-"*50)
        break
    else:
        print("Opção inválida.")







