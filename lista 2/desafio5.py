while True:
  numero=int(input("Digite um número:"))
  if numero == 2:
    print("primo")
    break
  
  if numero == 1:
    print("Número nao primo")
    break
  
  if numero %2 ==0:
    print("Número nao primo")
    break
    
  else:
    print("primo")
    break