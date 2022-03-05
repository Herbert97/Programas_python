#calculando un numero de la suerte dada la suma del año de nacimiento 
import math

nacimiento = int(input('Dame tu año de nacimiento'))
millares= nacimiento//1000
centenas = (nacimiento-(millares*1000))//100  
decenas = (nacimiento -(centenas*100+millares*1000))//10
unidades = nacimiento-(centenas*100 + decenas*10+millares*1000)
print(f'la fecha de nacimiento es:{nacimiento}')
print(f'millares: {millares}')
print (f'Centenas : {centenas}')
print(f'Decenas: {decenas}')
print(f'Unidades: {unidades}')

suerte=millares+centenas+decenas+unidades
print(f'el numero de la suerte es:{suerte}')