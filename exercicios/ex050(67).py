while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c:5} = {c*n:^5}')
print(f"NEGATIVO! Fim")        