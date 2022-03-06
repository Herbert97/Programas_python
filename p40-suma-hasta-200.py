c=s=0
while(True):
    n = int(input("Numero ?"))
    s += n
    c +=1
    if s == 200: break
print('Se introdujeron {0} numeros'.format(c))
print('La suma de los numeros es {0}'.format(s))
