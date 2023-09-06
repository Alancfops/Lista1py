import time
import os
while True:
    print("Conversor de graus")
    print("Opção 1 - Converter Fahrenheit para Celsius: ")
    print("Opção 2 - Converter Celsius para Fahrenheit: ")
    print("Opção 3 - Sair do conversor: " )
    op=input("Escolha uma opçao: ")

    if op == "1" :
        f=float(input("Digite a temperatura em Fahrenheit: ")) 
        celsius = (f - 32) * 5/9
        time.sleep(1.2)
        print(f"Fahrenheit {f} em celsius é : {celsius:5f}")
    elif op == "2":
        celsius=float(input("Digite a temperatura em Celsius: "))    
        f = (celsius*9/5) + 32
        time.sleep(1.2)
        print(f"Em celsius {celsius} equivale a {f} Fahrenheit")
    elif op == "3":
        print("Conversor finalizado")
        time.sleep(1.2)
        break
    else :
        print("Opção inválida")
if os.name == 'nt':
    os.system('cls')
    