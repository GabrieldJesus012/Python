
nint= int(input("Escreva um número inteiro:"))

print('''Escolha uma das base para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
[ 0 ] Sair''')

op= int(input("Sua Opção:"))

if op==0:
    print("Adeus")
elif op==1:
    print(bin(nint)[2:])
elif op==2:
    print(oct(nint)[2:])
elif op==3:
    print(hex(nint)[2:])
else:
    print("Opção Invalida.")