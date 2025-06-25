import interface

#programa principal

while True:
    escolha = interface.menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if escolha == "1":
        interface.lerCadastro()
    elif escolha == "2":
        interface.cadastro()
    elif escolha == "3":
        interface.cabecalho("Saindo do Sistema... até logo!")
        break
    else:
        print("Opção inválida.")







