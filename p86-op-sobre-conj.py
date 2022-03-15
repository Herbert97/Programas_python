# operaciones sobre conjuntos

import os 
os.system('cls')


print("Conjuntos y operaciones sobre ellos :")

municipios = {"Zacatecas", "Guadalupe","Jerez","Fresnillo"}
print(f"El conjunto original         : {municipios}")
print(f"Longitud del conjunto        : {len(municipios)}")
print(f"\nLa colección es del tipo   : {type(municipios)}")




print("\nLista de municipios usando un ciclo: ")
for m in municipios:
    print(m)

print(f"\nEsta Zacatecas en el conjunto: {'Zacatecas' in municipios}")

print("\nAgregra elementos a un conjunto:")
municipios.add("Teul")
print(f"Agregar con Add : {municipios}")

otrosmunicipios = {"Luis Moya","Ojocaliente","Tepetongo"}
municipios.update(otrosmunicipios)
print(f"Agregrar con Update : {municipios}")

print("\nEliminar elementos del conjunto:")
municipios.remove("Zacatecas") # genera error si no existe
print(f"Municipios : {municipios}")
municipios.discard("Ojocaliente") # si no esta no hace nada
print(f"Municipios : {municipios}")

m=municipios.pop() # elimina el tope = el primero
print(f"Municipios : {municipios}")
print(m)

municipios.clear()
print(f"Municipios : {municipios}")
