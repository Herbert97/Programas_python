# aceptar estudiante en base a cierto criterios
# mayores de edad y calificaciones >=8
print('bienvenido a la evaluacion de la  Universidad KITTY KAT SA ')

nombre = input('Dame tu nombre ? ')
print('masculino [M] y femenino [F]')
sexo= str.upper(input('cual es tu sexo? '))

if sexo=='F':
    edad = int(input('dame tu edad ? '))
    if edad>21 :
        print('Dame 3 calificaciones: ')
        c1,c2,c3= input().split()
        c1, c2, c3 = [float(c1),float(c2),float(c3)]
        promedio= (c1+c2+c3)/3
        print(f'promedio {promedio}')
        if promedio>8 or promedio>9.5:
            print(f'bienvenida {nombre} gracias por tu preferencia')
        else:
            print('solo aceptamos promedios entre 8 y 9.5')
    else:
        print('solo aceptamos mayores de 21 años')
else:
    print('solo aceptamos mujeres')