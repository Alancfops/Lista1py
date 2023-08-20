total = 0
p1 = str(input("TELEFONOU PARA A VITIMA?"))
if p1 == 'sim':
    total += 1
p2 = str(input("ESTEVE NO LOCAL DO CRIME?"))
if p2 == 'sim':
    total += 1
p3 = str(input("MORA PERTO DA VITIMA?"))
if p3 == 'sim':
    total += 1
p4 = str(input("DEVIA PARA A VITIMA?"))
if p4 == 'sim':
    total += 1
# nao lembro qual era a ultima pergunta
p5 = str(input("VOCE MATOU ELE?")) 
if p5 == 'sim':
    total += 1
if total == 0 or total == 1:
    print("Inocente")
if total == 2:
    print("Suspeito")
if total == 3 or total == 4:
    print("Cumplice")
if total == 5:
    print("Assasino")