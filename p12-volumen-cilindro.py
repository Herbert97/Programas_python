# calcula el volumen de un cilindro
import math
radio=int(input('dame el radio del cilindro'))
altura=int(input('dame la altura del cilindro'))

volumen=math.pi*(radio*radio)*altura
print(f'el volumen del cilindro es: {volumen}')