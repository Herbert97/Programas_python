# operaciones entre conjuntos de numeros

c1 = {1,2,3,4,5}
c2 = {5,6,7,8,9,10}
c3 = {9,10,11,12,13}
print(f"c1 : {c1} c2 : {c2} c3: {c3}")
#union

print("\nUnion: ")
c4 = c1.union(c2)
print(f"c1 union c2                  : {c4}")
c5 = c1 | c3
print(f"c1 union c3                  : {c5}")
c6 = set().union(c1).union(c2).union(c3)
print(f"c1 union c2 union c3: {c6}")

c4.clear();c5.clear();c6.clear()
#interseccion

print("\nIntersección: ")
c4 = c1.intersection(c2)
print(f"c1: {c1} inteseccion c2: {c2} = {c4}")
c5 = c2 & c3
print(f"c2: {c2} & c3: {c3} = {c5}")

c4.clear();c5.clear();c6.clear()
#diferencias

print("\nDiferencia:")
c4 = {3,4,5}
c5 = c1.difference(c4)
print(f"c1: {c1} diferencia c4: {c4} = {c5}")
c6 = c1 - c5
print(f"c1: {c1} - c5: {c5} = {c6}")

c4.clear();c5.clear();c6.clear()
#diferencias simetricas

print("\nDiferencia simetrica:")
c4 = c1.symmetric_difference(c2)
print(f"c1: {c1} diferenia simetrica c2: {c2} = {c4}")
c5 = c2 ^ c3
print(f"c2: {c2} diferenia simetrica c3: {c3} = {c5}")

print("\nAlgunos otros métodos:")
print(f"no tiene interseccion con c2:{c2} ? {c1.isdisjoint(c2)})")

#subconjunto y superconjunto

c4 = {1,3,5}
print(f"c4:{c4} es subconjunto de c1:{c1} :{c4.issubset(c1)} {c4<=c1}")
print(f"c1:{c1} es superconjunto de c4:{c4} :{c1.issuperset(c4)} {c1>=c4}")

print(f" 2 esta en {c1} ? : {2 in c1}")
print(f" 6 no esta en {c2} ? : {6 not in c1}")