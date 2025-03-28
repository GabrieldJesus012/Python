sexo = str(input("Informe o seu Sexo: [M/F]")).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input("Dados inválidos. Digite novamente o seu Sexo: [M/F]")).strip().upper()
print("Fim")