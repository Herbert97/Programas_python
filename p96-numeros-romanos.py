# crea un diccionario de numeros romanos y accede a ellos con numeros arabigos
numerosarabigos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numerosRomanos=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

numeros= dict(zip(numerosarabigos, numerosRomanos))
print(numeros)

n=int(input('dame un numero en arabigo que quieras: '))

print(f'el numero romano que elejiste es: {numeros.get(n)}')