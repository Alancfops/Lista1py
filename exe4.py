n1 = float(input("DIGITE SUA PRIMEIRA NOTA:"))
n2 = float(input("DIGITE SUA SEGUNDA NOTA:"))
media = (n1+n2)/2.0
if media == 10:
    print("APROVADO COM SUCESSO!")
elif media >= 7:
    print("APROVADO!")
else:
    print("REPROVADO!")