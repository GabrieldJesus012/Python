nome = input('Qual é o seu nome?')
print('Prazer em te conhecer {:20}!' .format(nome)) #20 caracteres
print('Prazer em te conhecer {:>20}!' .format(nome)) #20 c. alinhado a direita
print('Prazer em te conhecer {:<20}!' .format(nome)) #20 c. alinhado a esquerda
print('Prazer em te conhecer {:^20}!' .format(nome)) #20 c. alinhado no centro
print('Prazer em te conhecer {:=^20}!' .format(nome)) #20 c. alinhado no centro
print (f'Prazer em te conhecer {nome:=^20}!')
