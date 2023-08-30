numeros = []
while True:
    numero = input("Digite um número entre 0 e 1000 (ou 'sair' para sair): ")
    if numero == "sair" or numero == "Sair" or numero =="SAIR":
        break
    numero = float(numero)
    if numero >= 0 and numero <= 1000:
        numeros.append(numero)
    else:
        print("O número deve estar entre 0 e 1000.")

print("Menor valor:", min(numeros))
print("Maior valor:", max(numeros))
print("Soma dos valores:", sum(numeros))