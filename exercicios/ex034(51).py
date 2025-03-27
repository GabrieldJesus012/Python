print('='*20)
print("10 TERMOS DE UMA PA")
print('='*20)

n0=int(input("Primeiro Termo:"))
razao= int(input("Razão:"))
decimo = n0 + (10-1)*razao

for c in range(n0,decimo+razao,razao):
    print(f'{c}',end= " ->")
print('Acabou')