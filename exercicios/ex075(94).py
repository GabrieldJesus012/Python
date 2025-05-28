pessoas = []
soma_idade= 0
while True:
    dados = {}
    dados["nome"] = str(input("Nome: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
        dados["sexo"] = sexo
    dados["idade"] = int (input("Idade: "))
    soma_idade += dados["idade"]
    pessoas.append(dados.copy())
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer Continuar? [S/N]")).strip().upper()[0]
    if resp=="N":
        break
print("-="*40)
print(f"- O grupo tem {len(pessoas)} pessoas")
media = soma_idade/len(pessoas)
print(f'- A média de idade é de {media:.2f} anos')
print(f'- As mulheres cadastradas foram ', end="")
for p in pessoas:
    if p["sexo"] in "F":
        print(f"{p["nome"]} " , end="")
print()
print(f'- Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p["idade"]>=media:
        print(f'  -> Nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')

