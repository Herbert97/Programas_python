#secuencia de datos 
n=int(input('dame la cantidad de datos'))
suma=0
for i in range(1,n+1):
        suma+=(1/i)
        print(f'1/{i}+',end="")
print(f'  Suma : {suma}',end='')