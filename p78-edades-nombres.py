# nombres y edades
print("Introduce los nombres y edades: * en nombre termina\n")
nombres=[]
edades=[]
while True:
    nombre=input("Nombre: ")
    if nombre=="*":
        break
    else:
        nombres.append(nombre)
        edad=int(input("Edad: "))
        edades.append(edad)
print(f'Nombres: {nombres}')
print(f'Edades: {edades}')

print("\nAlumnos mayores de edad:")

for i in range(len(nombres)):
    if edades[i]>=18:
        print(f"Nombre: {nombres[i]} , Edad: {edades[i]}")

may=edades.index(max(edades))
print(f"Alumno de mayor edad: {nombres[may]}, {edades[may]}")