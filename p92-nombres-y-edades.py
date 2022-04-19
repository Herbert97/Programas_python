# Nombres y edades
datos = {}
print('Introduce nombres y edades * para terminar')
while True:
    nombre = input('Dame el nombre ? ')
    if nombre!='*':
        edad = int(input('Edad ? '))
        datos[nombre]=edad
    else:
        break
print(f'El diccionario de datos creado: {datos}')