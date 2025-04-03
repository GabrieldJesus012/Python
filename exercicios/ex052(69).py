print("-"*30)
print("Cadastre uma Pessoa")
print("-"*30)
mais18 = homem = mulheres20 = 0
while True:
    idade = int(input("Qual a sua idade?"))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Qual o seu sexo [M/F?] ")).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo in "M":
        homem += 1
    if idade < 20 and sexo in "F":
        mulheres20 += 1
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer Continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Homens cadastrados: {homem}')
print(f'Mulheres cadastradas menores que 20 anos: {mulheres20}')