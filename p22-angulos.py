# Muestra al tipo de angulo
# <90 agudo, =90 recto, >90 y <180 obtuso, =180 llano, >180 y <360 concavo
print('Mostrando el tipo de angulo en base a los grados')
angulo = int(input('Dame un angulo ?'))
print(f'El angulo tiene {angulo} grados por lo tanto es: ',end='')
if angulo < 90 :
    print(f'agudo')
elif angulo == 90 :
    print(f'recto')
elif angulo > 90 and angulo < 180 :
    print('obtuso')
elif angulo == 180 :
    print('llano')
elif angulo > 180 and angulo < 360 :
    print('concavo')
else :
    print('Angulo fuera de rango')