# aceptar estudiante en base a cierto criterios
# mayores de edad y calificaciones >=8

print('Evaluando estudiantes mayores de edad con calificaciones >=8')
nombre = input('Dame tu nombre ? ')
edad = int(input('dame tu edad ? '))

if edad>=18 :
    print('Dame 2 calificaciones: ')
    c1,c2= input().split()
    c1, c2 = [int(c1),int(c2)]
    if c1>=8 and c2>=8:
        print(f'{nombre} Bienvenido, edad {edad}, calificaciones {c1},{c2}')
    else:
        print('solo aceptamos calificaciones mayores a 8')
else :
    print('solo aceptamos mayores de edad')