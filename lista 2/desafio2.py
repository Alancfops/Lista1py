numeros = []
while True:
    numero = input("Digite um número (ou 'sair' para sair): ")
    if numero.lower() == "sair":
        break
    numeros.append(float(numero))

print("Menor valor:", min(numeros))
print("Maior valor:", max(numeros))
print("Soma dos valores:", sum(numeros))