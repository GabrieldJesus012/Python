alunos = []
dados = []
while True:
    dados.append(str(input("Nome: ")))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1+n2)/2
    dados.append(n1)
    dados.append(n2)
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer Continuar? [S/N]")).strip().upper()[0]
    if resp =="N":
        break
print("-=-"*20)
print(f"{'No.':<4} {'Nome':<10} {'Média':>6}")
print("-" * 25)
for indice, aluno in enumerate(alunos):
    print(f"{indice:<4} {aluno[0]:<10} {aluno[3]:>6.2f}")
while True:
    mostrar = int(input("Mostrar notas de qual aluno? [999 interrompe]"))
    if mostrar == 999:
        break
    if 0 <= mostrar < len(alunos):
        print(f'Notas de {alunos[mostrar][0]} são: {alunos[mostrar][1]}, {alunos[mostrar][2]}')
    else:
        print("Número inválido.")
