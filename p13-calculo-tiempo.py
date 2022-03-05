#convierte una cantidad de horas en su equivalente en dias, horas y minutos.

tiempo=int(input('dame la cantidad de horas'))

dias=tiempo/24
print(f'la cantidad de dias es: {dias}')

minutos=tiempo*60
print(f'la cantidad de minutos es: {minutos}')

segundos=minutos*60
print(f'la cantidad de segundos es: {segundos}')