print("m- MATUTINO, v- VESPERTINO, n - NORTURNO")
turno = str(input("QUE TURNO VC ESTUDA?"))
if turno == "m":
    print("Matutino!")
    print("Bom dia")
elif turno == "v":
    print("VESPERTINO!")
    print("Boa tarde")
elif turno == "n":
    print("Norturno")
    print("Boa noite")
else:
    print("Valor invalido")