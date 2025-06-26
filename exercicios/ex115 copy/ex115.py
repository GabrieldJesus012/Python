import interface
arq ="ex115.txt"
#programa principal
if not interface.arquivoExiste(arq):
    interface.criarArquivo(arq)

while True:
    escolha = interface.menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if escolha == 1:
        interface.lerCadastro(arq)
    elif escolha == 2:
        interface.cabecalho("Novo Cadastro")
        nome = str (input("Nome: ")).capitalize().strip()
        idade = interface.leiaInt("Idade: ")
        interface.cadastro(arq,nome,idade)
    elif escolha == 3:
        interface.cabecalho("Saindo do Sistema... até logo!")
        break
    else:
        print("Opção inválida.")







