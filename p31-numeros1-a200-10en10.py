# numeros de 1 a n de 10 en 10
n=int(input('hasta donde?'))
c = 1
while c < n:
    c += 1
    if c % 10: # if c/10 !=0 imprime el numero 
        continue
    print(c,end=' ') 