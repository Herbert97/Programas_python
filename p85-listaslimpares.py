# calcula de una lista de numeros impares para procesarlos.

n=int(input('dame un maximo de datos: '))
d=0
Lista=[]
for c in range(n):
    d+=1 
    Lista.append(d)

Lista2=[]
impares = [ n for n in Lista if n%2!=0]
print(f'impares : {impares}')
print(f'{Lista}')


suma=0
for n in impares:
    suma=suma+n
promedio= suma/len(impares)
print(f'la suma es {suma}')
print(f'el promedio es {promedio}')

divisibles=[]
sumadivisibles=0
for n in Lista:
    if n%3==0:
        divisibles.append(n)
        sumadivisibles=sumadivisibles+n
print(f'divisibles entre 3: {divisibles}')
print(f'la suma de los numeros divivisibles entre 3 es: {sumadivisibles} ')

buscar=int(input('dame el dato que quieres buscar en la primer lista: '))
print(f" el dato a buscar esta en {Lista} ? : {buscar in Lista}")
pos = Lista.index(buscar)
print(f'Que corresponde a la posicion: {Lista[pos]}')