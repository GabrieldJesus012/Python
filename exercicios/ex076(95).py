jogadores = []
while True:
    dados = {}
    gols = []
    dados["nome"] = str(input("Nome do Jogador: "))
    partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
    for c in range(0,partidas):
        gols.append(int(input(f"Quantos gols na partida {c}?")))
    dados["gols"] = gols[:]
    dados["total"] = sum(gols)
    jogadores.append(dados.copy())
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer Continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("-=-"*40)
print(f"{'cod.':<4} {'Nome':<10} {'Gols':>8} {'Total':>8}")
print("-"*40)
for i, a in enumerate(jogadores):
    print(f"{i:<4} {a['nome']:<10} {str(a['gols']):>10} {a['total']:>8}")
print('-='*40)
while True:
    qualjogador = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if qualjogador == 999:
        break
    if qualjogador >= len(jogadores):
        print(f"ERRO! Não existe jogador com código {qualjogador}! Tente novamente")
    else:
        print(f'O jogador {jogadores[qualjogador]["nome"]} jogou {len(jogadores[qualjogador]["gols"])} partidas.')
        for i, g in enumerate(jogadores[qualjogador]["gols"]):
            print(f'   => Na partida {i}, fez {g} gols.')
        print(f'Foi um total de {jogadores[qualjogador]["total"]} gols.')
        print('-=' * 40)