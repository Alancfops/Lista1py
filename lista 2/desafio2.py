numeros= []
while True: 
    numero=input('Digite um valor ( ou "sair" para finalizar): ')
    if numero.lower == "sair":
        break
    numeros.append(float(numero))

print("Menor o valor é:", min(numeros))    
print("Maior o valor é:", max(numeros))
print("Soma dos valores é:", sum(numeros))