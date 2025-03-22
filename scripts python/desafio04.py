import random
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = random.randint(0,2)
print('''Suas Opções
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
jogadajogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-='*11)

print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogadajogador]}')
print('-='*11)

if computador ==0: #pedra
    if jogadajogador ==0: #pedra
        print('EMPATE')
    elif jogadajogador ==1: #papel
        print('JOGADOR GANHOU')
    elif jogadajogador ==2: #tesoura
        print('JOGADOR PERDEU')
    else:
        print("Jogada Invalida")

elif computador ==1: #papel
    if jogadajogador ==0: #pedra
        print('JOGADOR PERDEU')
    elif jogadajogador ==1: #papel
        print('EMPATE')
    elif jogadajogador ==2: #tesoura
        print('JOGADOR GANHOU')
    else:
        print("Jogada Invalida")

elif computador ==2: #tesoura
    if jogadajogador ==0: #pedra
        print('JOGADOR GANHOU')
    elif jogadajogador ==1: #papel
        print('JOGADOR PERDEU')
    elif jogadajogador ==2: #tesoura
        print('EMPATE')
    else:
        print("Jogada Invalida")