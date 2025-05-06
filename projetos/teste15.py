num = [2,3,4]
num [2]=1
print(num)
num.append(10)
print(num)
num.sort()
print(num)
num.insert(2,0)
print(num)
num.pop()
print(num)
num.insert(2,2)
print(num)
num.remove(2)
print(num)
if 5 in num:
    num.remove(5)
else:
    print("Não achei o número 5")
print(f"Essa lista tem {len(num)} elementos")

