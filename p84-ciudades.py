#lee una cantidad de ciudades hasta introducir $ imprime cuantos son y la lista completa
print('Introduce el nombre de ciudades introducir & para terminar:')
ciudades=[]
n=''
ciudades2=[]
vocales='''A E I O U'''
while n!='&':
    n=input('dame la ciudad: ')
    ciudades.append(n)
    ciudades2.append(n)

    if n.startswith('A'):
        ciudades2.remove(n)
    if n.startswith('E'):
        ciudades2.remove(n)
    if n.startswith('I'):
        ciudades2.remove(n)
    if n.startswith('O'):
        ciudades2.remove(n)
    if n.startswith('U'):
        ciudades2.remove(n)

ciudades2.remove('&')
ciudades.remove('&')
print(f'ciudades{ciudades}:')
print(f'cantidad de ciudades: {len(ciudades)}')
ciudades.sort(reverse=True)
print(f'orden descendente:{ciudades}')
print(f'ciudades que empiezan con consonantes: {len(ciudades2)}: {ciudades2} ')

