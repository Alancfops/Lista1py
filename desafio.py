senha = "1234"
total = 0
while total < 4:
    senha = input("Digite sua senha:")
    total += 1
    if senha == "1234":
        print("Acesso permitido")
        break
    elif total == 3:
        print("Resta mais uma chance:")
    elif total == 4:
        print("Acesso negado")
    else:
        print("Senha incorreta")