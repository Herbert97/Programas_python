# Este módulo contiene funciones para el manejo de
# una lista de diccionarios
from operator import itemgetter
"""
Recibe una lista de diccionarios y un campo
Regresa el valor promedio de la lista en ese campo
"""
def valor_promedio(poblacion, campo):
    s = 0
    for j in poblacion:
        s += j[campo]
    return s / len(poblacion)

"""
Recibe una lista de diccionarios y un campo
Regresa el valor mayor de la lista en ese campo
"""
def valor_mayor(poblacion, campo):
    m = poblacion[0][campo]
    jm = [{}]
    for j in poblacion:
        if j[campo] > m:
            jm[0]=j
    return jm

"""
Recibe una lista de diccionarios y un campo
Regresa el valor menor de la lista en ese campo
"""
def valor_menor(poblacion, campo):
    m = poblacion[0][campo]
    jm = [{}]
    for j in poblacion:
        if j[campo] < m:
            jm[0]=j
    return jm

"""
Recibe una lista de diccionarios, un campo, y tipo de orden
Ordena e imprime la lista en base al campo y tipo de orden
"""
def imprime(poblacion, campo, ascdec):
    if campo!='':
        poblacion = sorted(poblacion, key=itemgetter(campo),reverse=ascdec)
    print(f"{'Pais':>6} {'2018':<4} {'2019':>4} {'2020':>4} {'2021':>4}")
    for j in poblacion:
        print(f"{j['pais']:>6} {j['2018']:<4} {j['2019']:>4} {j['2020']:>4} {j['2021']:>4}")