# calculando el numero mayor de una serie de numeros
mayor=0
import os
while(True):
    n=int(input('numero ?'))
    if n==0: break
    if n>mayor:
        mayor=n
print(f'mayor {mayor}')

    
    