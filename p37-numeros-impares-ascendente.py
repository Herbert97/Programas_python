#impresion de numeros impares de forma ascendete
print('impresion de numeros de manera ascendente')
n=int(input('numero al que desea llegar'))

i = 1
s = 0
while i<=n:
    print(i, end=' ')
    if i%2 != 0:
        s = s + i
    i+=1
print (f'La suma  de números impares es:{s}')