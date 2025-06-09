def ficha(jogador="<desconhecido>",gol =0):
    print(f'O jogador {jogador} fez {gol} gols(s) no campeonato.')

nome = str(input("Nome do Jogador: ")).strip()
gols = str(input("Número de Gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(gol=gols)
else:
    ficha(nome,gols)
