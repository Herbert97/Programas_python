# Este módulo contiene funciones para el manejo de
# una lista de diccionarios con jugadores de la fifa

from operator import itemgetter
"""
Recibe una lista de diccionarios y un campo
Regresa el valor promedio de la lista en ese campo
"""
def valor_promedio(fifa, campo):
    s = 0
    for j in fifa:
        s += j[campo]
    return s / len(fifa)

"""
Recibe una lista de diccionarios y un campo
Regresa el valor mayor de la lista en ese campo
"""
def valor_mayor(fifa, campo):
    m = fifa[0][campo]
    jm = [{}]
    for j in fifa:
        if j[campo] > m:
            jm[0]=j
    return jm

"""
Recibe una lista de diccionarios y un campo
Regresa el valor menor de la lista en ese campo
"""
def valor_menor(fifa, campo):
    m = fifa[0][campo]
    jm = [{}]
    for j in fifa:
        if j[campo] < m:
            jm[0]=j
    return jm

"""
Recibe una lista de diccionarios, un campo, y tipo de orden
Ordena e imprime la lista en base al campo y tipo de orden
"""
def imprime(fifa, campo, ascdec):
    if campo!='':
        fifa = sorted(fifa, key=itemgetter(campo),reverse=ascdec)
    print(f"{'Id':>6} {'Nombre':<35} {'Valeuros':>10} {'Edad':>4} {'Peso':>4} {'Nacionalidad':<15}")
    for j in fifa:
        print(f"{j['id']:>6} {j['nombre']:<35} {j['valeuros']:>10} {j['edad']:>4} {j['peso']:>4} {j['nacionalidad']:<15}")
