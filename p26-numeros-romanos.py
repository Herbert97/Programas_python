# convierte numeros decimales a numeros romanos
print('equivalentes de numero decimales a romanos')
numero=int(input('dame un numero entre el 1 y 10 '))
if numero<=10:
    if numero== 1:
        print('tu numero romano es I')
    elif numero== 2:
        print('tu numero romano es II')
    elif numero== 3:
        print('tu numero romano es III')
    elif numero==4:
        print('tu numero romano es IV')
    elif numero==5:
        print('tu numero romano es V')
    elif numero==6:
        print('tu numero romano es VI')
    elif numero==7:
        print('tu numero romano es VII')
    elif numero==8:
        print('tu numero romando es VIII')
    elif numero==9:
        print('tu numero romando es IX')
    elif numero==10:
        print('tu numero romano es X')
else:
    print('pilluelo ingresaste un numero fuera del rango')