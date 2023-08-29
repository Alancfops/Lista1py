numeros= []
while True: 
    numero=input('Digite um valor ( ou "sair" para finalizar): ')
    if numero.lower == "sair":
        break
    if numero>=0 and numero<=1000:
        numeros.append(float(numero))
    else:
        print("Tem que ser um número e deve estar entre 0 e 1000")

        

print("Menor o valor é:", min(numeros))    
print("Maior o valor é:", max(numeros))
print("Soma dos valores é:", sum(numeros))
