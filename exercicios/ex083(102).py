def fatorial(num,show=False):
    '''
    -> Calcula o fatorial de um número.
    :para n: o número a ser calculado.
    :para show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    '''
    import math
    print("-"*20)
    if show==True:
        f=1
        c=num
        while c>0:
            print(f'{c}',end="")
            print(f' x ' if c>1 else " = ",end="")
            f*=c
            c-=1
        return f
    else:
        return math.factorial(num)

help(fatorial)
print(fatorial(5,show=False))
print(fatorial(5,show=True))

'''
for c in range(num, 0, -1):
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c

print(f"{f}")
'''