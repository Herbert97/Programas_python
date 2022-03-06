# conversion de grados celcius a grados farenheit en lista
print('comienza la lista de conversion de grados celcius a grados')
n=int(input('ingresa el valor  con el que quieres empezar la conversion'))
j=int(input('ingresa el valor maximo de la lista de conversion'))
conversion=0
while n<=j:
    print(f'los grados centigrados son: {n}')
    conversion = (n * 9 / 5 ) + 32
    print(f'la conversion de temperatura es {conversion}')
    n+=1
