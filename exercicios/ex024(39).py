import datetime
anonasc = int(input('Que ano você nasceu: '))
anohoje = datetime.date.today().year
idade=anohoje-anonasc
minalistamento =18

print(f'Quem nasceu em {anonasc} tem {idade} anos em {anohoje}')

if idade<18:
    print(f'Você ainda vai se alistar, falta {minalistamento-idade} ')
elif idade==18:
    print(f'Se lascou, vai se alistar vagabundo!')
else:
    print(f'Sortudo, já passou o tempo de alistamento há {idade-minalistamento} anos')