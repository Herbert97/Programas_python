# cuadro de asteriscos
r = int(input('Cuantos renglones ? '))
c = (input('Caracter ? '))
for i in range(1,r+1):
    for j in range(1,r+1):
        print(c, end='')
    print('')