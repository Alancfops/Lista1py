numero = []
cont = 1
while cont <=3:
    print(f"Nota {cont}")
    nota = float(input("Digite sua nota: "))  
    numero.append(nota)
    cont +=1
sum(numero)
total= sum(numero)
media = total / 3 

if media >= 7:
    print("Aprovado!!")
elif media <=7 and media>=4:
    print("Reposição")
else :
    print("Reprovado!!")    