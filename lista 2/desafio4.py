while True:
  nome = (input("Digite o nome (maior que 3 caracteres):"))
  if len(nome) >3:
    print("Valido!")
    break
  else:
    print("Digita novamente:")
  
while True:
  idade = int(input("Digite sua idade:"))
  if idade >=0 and idade <=150:
    print("Valido")
    break
  else:
    print("Idade invalida, Digite novamente:")

while True:    
  salario = float(input("Digite seu salario:")) 
  if salario > 0:
    print("Valido")
    break
  else:
    print("Salario invalido, digite novamente:")

while True:
  sexo = str(input(("Digite seu genero (F para feminino e M para masculino):")))
  if sexo.lower() == 'f' or sexo.lower() == 'm':
    print("Valido")
    break
  else:
    print("Tente novamente!")

while True:
  estadocivil =str(input("Digite seu estado civil (S- solteiro, C- casado, D- divorciado, V - viuvo):"))
  if estadocivil.lower() =='s' or estadocivil.lower() =='c' or estadocivil.lower() =='d' or estadocivil.lower() == 'v':
    print("Valido")
    break
  else:
    print("Tente novamente:")