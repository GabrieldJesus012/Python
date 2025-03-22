import datetime
anonasc = int(input('Que ano você nasceu: '))
anohoje = datetime.date.today().year
idade = anohoje - anonasc

#print(f'O atleta tem {idade}anos')

if idade <= 9:
    print(f'''o atleta tem {idade}
    Classificação: Mirim''')
elif idade <= 14:
    print(f'''o atleta tem {idade}
    Classificação: Infantil''')
elif idade <= 19:
    print(f'''o atleta tem {idade}
    Classificação: Junior''')
elif idade<=20:
    print(f'''o atleta tem {idade}
    Classificação: Senior''')
else:
    print(f'''o atleta tem {idade}
    Classificação: MASTER''')
