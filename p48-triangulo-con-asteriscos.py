# triangulo de asteriscos
n = int(input('Cuantos renglones ? '))
c= input('caracter ?')
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c, end="")
    print("\r")