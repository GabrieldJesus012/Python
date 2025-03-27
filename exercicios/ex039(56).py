somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=''
totmulher=0

for pess in range(1, 3):
    print(f'---{pess}ª PESSOA ----')
    nome = str(input(f"Qual o seu Nome {pess}ª pessoa?")).strip()
    idade = int(input(f"Qual a sua idade {nome}?"))
    sexo = str(input(f"Qual o seu sexo {nome} [M/F?] ")).strip()
    somaidade +=idade
    if pess ==1 and sexo in "Mm":
        maioridadehomem=idade
        nomevelho=nome
    if sexo in "Mm" and idade>maioridadehomem:
        maioridadehomem= idade
        nomevelho=nome
    if sexo in "Ff" and idade<20:
        totmulher +=1
mediaidade=somaidade/4
print(f'A media de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos')
print(f'Ao todo são {totmulher} com menos de 20 anos')