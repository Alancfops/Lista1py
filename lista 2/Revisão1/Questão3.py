limite=int(input("Digite o número para o limite da sequencia: "))
print("O dobro dos números de 1 até o limite da sequencia")

cont =1
while cont <= limite:
    dobro= cont * 2
    print(f"{cont} : {dobro}")
    cont += 1