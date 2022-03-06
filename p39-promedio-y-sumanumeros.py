# cuenta suma, promedio
c=s=0

while(True):
    n = int(input("Numero ?"))
    if n == 0: break
    s += n
    c +=1
    promedio=s/c
print('Se introdujeron {0} numeros'.format(c))
print('La suma de los numeros es {0}'.format(s))
print(f'el promedio es: {promedio}')
