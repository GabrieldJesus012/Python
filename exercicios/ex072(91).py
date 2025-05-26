import random
import time
from operator import itemgetter
jogo = {}
ranking = ()
for c in range (5):
    jogo[f'jogador{c}'] = random.randint(1,6)
print("Valores Sorteados:")
for k,v in jogo.items():
    print(f'o {k} tirou {v} no dado')
    time.sleep(0.5)
ranking = sorted(jogo.items(), key= itemgetter(1),reverse=True) #itemgetter (0) = chave // (1) = Valor
print("Ranking dos Jogadores:")
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    time.sleep(0.5)
