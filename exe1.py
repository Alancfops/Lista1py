n1 = float(input("Digite seu numero:"))
n2 = float(input("Digite seu outro numero:"))
n3 = float(input("Digite outro numero:"))
print("Seus numeros foram {} e {} e {}".format(n1, n2, n3))
if n1 > n2 and n3:
    print("{} ,esse numero foi maior!".format(n1))
elif n2 > n3:
    print("{} ,esse numero foi maior!".format(n2))
else:
    print("{} ,esse numero foi maior!".format(n3))
