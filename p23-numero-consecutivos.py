# determina si 3 numeros son consecutivos
print('dame tres numeros separados por una linea: ')
n1, n2, n3 = int(input()), int(input()), int(input())
if n3-1 == n2:
    #print('los digitos 3 y 2 son consecutivos')
    if n2-1==n1:
        print('gracias')
else :
    print('error los 3 numeros no son consecutivos')
