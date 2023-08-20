print('-'*20)
letra = (input)("Digite uma Letra:")
print("Suas letras foram {}".format(letra))
if letra in 'aeiou' or 'AEIOU':
    print("é uma vogal!")
    print('-'*20)
else:
    print("é uma consoante!")
    print('-'*20)