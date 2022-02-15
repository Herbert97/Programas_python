# Calcular la suma y el promedio de tres calificaciones

print('Calculando el promedio de 3 calificaciones')
print('dame tres calificaciones separadas por un espacio: ')
c1,c2,c3 =input().split()
c1,c2,c3 = [float(c1), float(c2), float(c3)]
suma =  c1 + c2 + c3
promedio = suma/ 3
print(f'El promedio de: {c1}, {c2} y {c3} es {suma} y el promedio es {promedio}')

