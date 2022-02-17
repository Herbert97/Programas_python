# Verificar si al suma de dos numeros es igual a un tercero

print('Verificando si la suma de dos numeros es igual a un tercero')

print('Dame 3 numeros enteros separados por una linea: ?')

n1, n2, n3 = int(input()), int(input()), int(input())
if n1 + n2 == n3 :
    print('Son iguales')
else :
    print('Son distintos')