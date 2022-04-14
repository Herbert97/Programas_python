#lee dos listas con 5 elementos y las multiplica.
print('introduce los primeros 5 elementos')
L1=[]
n=0
limite=5
for n in range(1,limite+1):
    n = float(input("dame la calificacion > "))
    if n>=0 and n<=10:
        L1.append(n)
    else:
        print('no se encuentra dentro del rango')
print('Fin de la primer lista' )  
print(f'{L1}')

L2=[]
y=0
limite=5
for y in range(1,limite+1):
    n = float(input("dame la calificacion > "))
    if n>=0 and n<=10:
        L2.append(n)
    else:
        print('no se encuentra dentro del rango')
print('Fin de la segunda lista')  
print(f'{L2}')

lista3=[]
for i in range(limite):
    lista3.append(L1[i]*L2[i])
print(f'\nLista3 multiplicacion : {lista3}')