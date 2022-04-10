# procesar texto
txt = '''Aprender a programar en python es una tarea \
que requiere tiempo y constancia, la practica \
es lo que da la experiencia'''
print(f'Frase: {txt}')
pal = input('Dame una palabra ? ')

pos = txt.find(pal)
if pos!= -1:
    if txt.startswith(pal):
        print(f'{pal}: es la primer palabra de la frase')
    elif txt.endswith(pal):
        print(f'{pal}: es la ultima palabra de la frase')
    else:
        print(f'{pal}: aparece la primera vez en la posición: {pos} de la frase')
        print(f'{pal}: aparece {txt.count(pal)} veces en la frase')
        txt2 = txt.replace(pal,'##')
        print(f'Frase Modificada: {txt2}')
else:
    print(f'{pal} no se encuentra en la frase')
    
print('\nProcesamiento de la frase:')
print(f'Mayusculas: {txt.upper()}')
print(f'Minusculas: {txt.lower()}')
print(f'Titulo : {txt.title()}')
txt3 = txt.split()
print(f'Separar : {txt3}')
print(f'Unir : {"-".join(txt3)}')