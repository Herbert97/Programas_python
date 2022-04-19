# Estudiantes
estudiante = {
'nombre':'Carlos',
'edad':45,
'email':'castr@hotmai.com',
'carrera':'Sistemas'
}
print(f'\nEl diccionario: {estudiante}')

print('\nLas llaves: ')
for k in estudiante.keys():
    print(k)

print('\nLos valores: ')
for v in estudiante.values():
    print(v)
    
print("\nLlaves y valores:")
for k,v in estudiante.items():
    print(f'{k:<10} : {v}')
estudiante['calificacion']=9.5
print(f'\nEl diccionario actualizado: {estudiante}')