#impresion de secuencia de terminos 1+11+111+111 
n=int(input('dame la cantidad de datos'))
suma=0
for i in range(1,n+1):
    print('+',end="")
    for j in range(1,i+1):
        print(1,end='')

print(f'  Suma : {n}',end='')
