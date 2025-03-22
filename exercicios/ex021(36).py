valorcasa= float(input("Qual o valor da casa: R$"))
salario= float(input("Qual o seu salário? R$"))
anospag= int(input("Em quantos anos você deseja pagar?"))

prestm = valorcasa/(anospag*12)
min = salario*0.3

if prestm>=min:
    print(f'para pagar uma casa de R${valorcasa:.2f} em {anospag} anos a prestação será de R${prestm:.2f}! Emprestimo Negado, mínimo {min:.2f}')
else:
    print(f'para pagar uma casa de R${valorcasa:.2f} em {anospag} anos a prestação será de R${prestm:.2f}! Emprestimo Aprovado, mínimo {min:.2f}')
