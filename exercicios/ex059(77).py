palavras = ("APRENDER","PROGRAMAR","LINGUAGEM","PYTHON",
            "CURSO","GRATIS","ESTUDAR","PRATICAR","TRABALHAR",
            "MERCADO","PROGRAMADOR","FUTURO")
vogais = "AEIOU"
for cont in palavras:
    print(f"\nNa palavra {cont} temos ", end="")
    for letra in cont:
        if letra in vogais:
            print(letra, end=" ")