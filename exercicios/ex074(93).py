dados = {}
gols = []
dados["nome"] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
for c in range(0,partidas):
    gols.append(int(input(f"Quantos gols na partida {c}?")))
dados["gols"] = gols
dados["total"] = sum(dados["gols"])
print(dados)