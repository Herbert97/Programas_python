# Lee datos y venvia un saludo


print('Leyendo datos por teclado y enviar saludo a pantalla')
nombre = input('Dame tu nombre?')
edad= int(input('dame tu edad'))
peso = int(input('Dame tu peso'))
print('Bienvenido',nombre,'tu edad es',edad,'tu peso es',peso)
print(f'Bienvenido{nombre} tu edad es {edad} tu peso es {peso}')
print(type(nombre))
print(type(edad))
print(type(peso))