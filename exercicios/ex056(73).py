times= ("Palmeiras","Flamengo","Fluminense","Bragantino","Ceará SC","Corinthians",
        "Cruzeiro","Vasco da Gama","Juventude","São Paulo","Mirassol","Internacional",
        "Bahia","Fortaleza","Botafogo","EC Vitória","Atlético MG","Santos","Grêmio","Sport Recife")
print("-=-"*20)
print(f"Lista de Times do Brasileirão:{times}")
print("-=-"*20)
print(f"Os cincos primeiros são: {times[0:5]}")
print("-=-"*20)
print(f"Os quatro últimos são: {times[-4:]}")
print("-=-"*20)
print(f"Times em Ordem Alfabética: {sorted(times)}")
print("-=-"*20)
print(f"O Bragantino está na {times.index("Bragantino")+1}ª posição")
