# mes dias y nombre lee un numero de mes eh imprime un dias del mes y el nombre
print('Seleccionar mes')

Dias=[31,28,31,30,31,30,31,31,30,31,30,31]
mes=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
n=int(input('dame un numero entre 1 y 12: '))
print(f'seleccionaste el mes: {mes[n-1]}')
print(f'el cual contiene una cantidad de:{Dias[n-1]} Dias')

