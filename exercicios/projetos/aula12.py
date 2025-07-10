nome = str(input("Qual é o seu nome?")).lower().strip()

if nome == "gabriel":
    print("Que nome Bonito")
elif nome == "pedro" or nome == "maria" or nome == "paula":
    print("Seu nome é bem normal no Brasil")
elif nome in "ana claudia juliana":
    print ("Belo nome feminino")
else:
    print("Seu nome é bem normal")
print(f'Tenha um bom dia {nome}')
