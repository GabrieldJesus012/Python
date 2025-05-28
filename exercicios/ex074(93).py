dados = {}
gols = []
dados["nome"] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
for c in range(0,partidas):
    gols.append(int(input(f"Quantos gols na partida {c}?")))
dados["gols"] = gols[:]
dados["total"] = sum(dados["gols"])
print('-='*40)
print(dados)
print('-='*40)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*40)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i,v in enumerate (gols):
    print(f"=> Na partida {i} fez {v} gol")
print(f"Foi um total de {dados['total']} gols")
