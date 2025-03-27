from time import sleep
n = int(input("Digite um número inteiro: "))
print("-=-" * 20)
sleep(0.5)
print('ANALISANDO')
sleep(0.5)
print("-=-" * 20)

total = 0
for c in range(1, n + 1):
    if n % c == 0:  
        total += 1
        print(f'\033[33m{c}\033[m', end=' ')  # Números divisíveis em amarelo
    else:
        print(f'\033[31m{c}\033[m', end=' ')  # Números não divisíveis em vermelho
print(f'\nO número {n} foi divisível {total} vezes')

if total == 2:  
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')
print('FIM')