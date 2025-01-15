import random
nam = (random.randint(0,5))
print('-=-' *20)
print('Qual o número entre 0 e 5 que estou pensando!')
print('-=-' *20)
num = int(input('Qual você escolhe? '))
if num == nam:
    print(f'Parabens, você acertou! o computador pensou em {nam}')
else:
    print(f"ERROUUUUUUUU, você pensou em {num} mas era {nam}")
