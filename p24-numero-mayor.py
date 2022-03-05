# identifica el numero mayor entre 3 numeros
print('dame tres numeros separados por una linea: ')
n1, n2, n3 = int(input()), int(input()), int(input())
if n1>n2:
    if n1>n3:
        print(f'el numero mayor es el primero: {n1}')
elif n2>n3:
    if n2>n1:
        print(f'el numero mayor es el segundo: {n2}')
elif n3>n2:
    if n3>n1:
        print(f'el numero mayor es el tercero: {n3}')
else:
    print('los numeros son iguales')