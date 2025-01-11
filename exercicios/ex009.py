import random
a0= str(input('Primeiro aluno: '))
a1= str(input('Segundo aluno: '))
a2= str(input('Terceiro aluno: '))
a3= str(input('Quarto aluno: '))
alunos = [a0,a1,a2,a3]
print('O aluno escolhido foi {}'.format(random.choice(alunos)))
random.shuffle(alunos)
print('A ordem de apresentação será {}'.format(alunos))
