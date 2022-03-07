#secuencia de n numeros V2

n = int(input('Cuantos renglones ? '))
for i in range(1,n+1):
    k=0
    for j in range(1,i+1):
        k+=1
        print(k, end="")
    print("\r")