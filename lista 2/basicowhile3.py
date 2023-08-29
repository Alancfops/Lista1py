print('Calculadora de adição')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

total = n1+n2
print(f'{n1} + {n2} = {total}')

continuar = input('Quer continuar as contas? [S=Sim ou N=Não]: ')

while continuar == 'S' or continuar =='s':
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite mais um número: '))
    total = n1+n2
    print('{} + {} = {}'.format (n1, n2, total))
    continuar = input('Quer continuar as contas? [S=Sim ou N=Não]: ')