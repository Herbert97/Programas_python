# realiza el promedia de 5 notas y identifica si se aprobo
print('calculando el promedio de 5 calificaciones')
print('Dame 5 calificaciones separadas por espacio: ')
c1,c2,c3,c4,c5= input().split()
c1,c2,c3,c4,c5 = [float(c1),float(c2),float(c3),float(c4),float(c5)]

promedio=(c1+c2+c3+c4+c5)/5
print(f'promedio {promedio}')
if promedio>6:
    if promedio==10 or promedio>9:
        print('perfecto tu esfuerzo valio la pena')
    elif promedio==9 or promedio>8:
        print('excelente sigue asi') 
    elif promedio==8 or promedio>7:
        print('muy bien,pues mejorar')
    elif promedio==7 or promedio>6:
        print('pasas de panzazo')
else:
    print('reprobado')

    