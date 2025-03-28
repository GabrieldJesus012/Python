import random
nam = (random.randint(0,5))
print('-=-' *20)
print('Qual o número entre 0 e 5 que estou pensando!')
print('-=-' *20)
num = int(input('Qual você escolhe? '))
tentativas= 0

while (num!=nam):
    print("Errou, tente novamente")
    tentativas+=1
    if num < nam:
        print("DICA: Mais...")
    else:
        print("DICA: Menos...")
    num = int(input('Qual você escolhe? '))
print(f'Parabens, você acertou! o computador pensou em {nam} e utilizou {tentativas} tentativas')
