dados = {}
gols = []
time = []
while True:
    dados.clear()
    dados["nome"] = str(input("Nome do Jogador: "))
    partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
    gols.clear()
    for c in range(0,partidas):
        gols.append(int(input(f"Quantos gols na partida {c+1}?")))
    dados["gols"] = gols[:]
    dados["total"] = sum(gols)
    time.append(dados.copy())
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer Continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("-="*40)
print('cod ',end="")
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
print("-"*40)
for k,v in enumerate(time):
    print(f'{k:>3}',end="")
    for d in v.values():
        print(f'{str(d):<15}',end="")
    print()
print('-='*40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(dados):
        print(f"ERRO! Não existe jogador com código {busca}! Tente novamente")
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i,g in enumerate(time[busca]['gols']):
            print(f'   => Na partida {i+1}, fez {g} gols.')
    print("-"*40)