# impresion de numeros de manera descendente

n=int(input('hasta donde el contador?'))
c = 100
s=0
while c >= n :
    print(c, end=' ')
    if c%2 == 0:
        s = s + c
    c -= 1
print(f'la suma de numeros pares es {s}')