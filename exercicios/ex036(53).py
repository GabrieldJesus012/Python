frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)  
inverso = ''

# Cria o inverso usando for
for letra in range(len(junto) - 1, -1, -1): #comeca na ultima letra, vai até -1 (primeira letra 0) e inverso
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase NÃO é um PALÍNDROMO!')


