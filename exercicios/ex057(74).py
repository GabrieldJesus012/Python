import random
maior = menor = 0
num = (random.randint(0, 10),random.randint(0, 10),
        random.randint(0, 10),random.randint(0, 10),random.randint(0, 10))
print('Os valores sorteados são: ',end="")
for n in num:
    print(f'{n}',end=" ")
print(f"\nO maior sorteado foi {max(num)}")
print(f"O menor sorteado foi {min(num)}")

