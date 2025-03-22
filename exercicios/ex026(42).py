s1=float(input('Primeiro Segmento:'))
s2=float(input('Segundo Segmento:'))
s3=float(input('Terceiro Segmento:'))

if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('Os segmentos acima podem formar um triângulo!',end='')
    if s1==s2==s3:
        print(" Todos os lados são iguais, é um EQUILATERO")
    elif s1==s2 or s2==s3 or s1==s3: 
        print(' Dois lados são iguais, é um ISÓSCELES')
    elif s1 != s2 and s2 != s3 and s1 != s3: #ou s1 != s2 != s3 != s1
        print(' Todos os lados são diferente, é um ESCALENO')
else:
    print("Não podem formar um triângulo esses segmentos")