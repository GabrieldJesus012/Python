import datetime
dados = {}
dados["nome"] = str(input("Nome: "))
ano = datetime.date.today().year
nasc = int(input("Ano de Nascimento: "))
dados["idade"] = ano - nasc
dados["ctps"] = int(input("Carteira de Trabalho (0 nao tem): "))
if dados["ctps"] != 0:
    dados["contratação"] = int (input("Ano de Contratação: "))
    dados["salário"] = float(input("Sálario: R$"))
    #se aposenta com 35 anos de colaboração
    anos_contribuidos = ano - dados["contratação"]
    anos_que_faltam = 35 - anos_contribuidos
    if anos_que_faltam > 0:
        dados["aposentadoria"] = dados["idade"] + anos_que_faltam
    else:
        dados["aposentadoria"] = dados["idade"] 
for k,v in dados.items():
    print(f"- {k} tem o valor de {v}")
