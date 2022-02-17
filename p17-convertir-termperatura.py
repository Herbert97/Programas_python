# Conversión de temperaturas de Centigrados a Farenheit y viceversa

print('Conviritiendo temperaturas de centigrados a farenheit ...')
print('[C] entigrados')
print('[F] farenheit')
print('Elige una opcion ?')

opcion = str.upper( input())
if opcion == 'C':
    print('\nConvirtiendo a Centigrados ...')
    temp = float(input('Grados Farenheit ?'))
    res = (temp - 32) * 5 / 9
    print(f'{temp} grados Fahrenheit, equivalen a {res} grados Centigrados')
else :
    print('\nConviritiendo a Farenhet...')
    temp = float(input('Dame los Centigrados ?'))
    res = ( temp * 9 / 5 ) + 32
    print(f'{temp} grados Fahrenheit, equivalen a {res} grados Centigrados')
print('\nGracias por utilizar este programa...')