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
    return opc

#arquivo
def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome,'wt+') # o + é para criar
        a.close()
    except:
        print("Houve um erro ao criar o arquivo")
    else:
        print(f'Arquivo {nome} criado com sucesso')

def cadastro (arq,nome="Desconhecido",idade = 0):
    try:
        a = open(arq,'at') #adiciona algo ao arquivo
    except:
        print ("Houve um erro na abertura do arquivo")
    else:
        try:
            a.write (f'{nome};{idade}\n')
        except:
            print("Houve um erro na hora de escrever os dados")
        else: 
            print(f"Registro de {nome} adicionado com sucesso!")

def lerCadastro(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo.")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado =linha.split(';')
            dado[1] = dado [1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
