#lista de nombres y operaciones entre ellas

lista1={"Juan", "Maria", "Jose", "Rocio"}
lista2={"Pedro","Juan","Pablo","Mateo","Esther"}

print(f'los nombres de la primer lista son: {lista1} ')
print(f'los nombres de la segunda lista son: {lista2}')

print('union entre las listas')
L1=lista1.union(lista2)
print(f'{L1}')

print('interseccion entre las listas')
L2=lista1.intersection(lista2)
print(f'{L2}')

print('diferencia entre listas')
L3=lista1.difference(lista2)
print(f'{L3}')

print(f'diferencia simetrica entre listas')
L4=lista1.symmetric_difference(lista2)
print(f'{L4}')


print('Subconjuntos')
c4={"Pablo","Mateo"}
print(f"Pablo y Mateo:{c4} es subconjunto de Lista 2:{lista2} :{c4.issubset(lista2)} {c4<=lista2}")

print('Superconjunto')
c3={"Reynaldo","Angelica"}
print(f":{lista1} es superconjunto de c4:{c3} :{lista1.issuperset(c3)} {lista1>=c3}")

c1={'Pedro'}
print(f" Pedro esta en {lista1} ? : {c1 in lista1}")

c2={'Lilia'}
print(f" Lilia esta en {lista2} ? : {c2 in lista2}")