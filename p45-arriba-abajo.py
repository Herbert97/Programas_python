# numeros del 1 a n o de 100 al n
import os
os.system('cls')
op=int(input('[1] ir arriba \n [2] ir abajo ?'))
if op==1:
    print('imprimiendo hacia arriba...')
    n=int(input('hasta donde quieres llegar?'))
    i= int(input('incrementos?'))
    for x in range (1,n+1,i):
        print(x,end=' ')
elif op==2:
    print('imprimiendo hacia abajo..')
    n=int(input('hasta donde quieres llegar?'))
    i=int(input('Decremento?'))
    for x in range(n,0,i):
        print(x,end=' ')    
