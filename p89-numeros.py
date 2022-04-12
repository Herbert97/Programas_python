#lista de numero y operaciones entre ellos.
A={50,60,70,80,90,100,200}
B={60,90,100,300,400,500}
C={10,20,60,90,70,100,600,700}
print(f'la primer lista: {A} la seguda lista: {B} la tercer lista{C}')

uab=A.union(B)
print(f'union de A y B: {uab}')
ubc=B.union(C)
print(f'union de B y C: {ubc}')

dac=A.difference(C)
print(f'diferencia A y C: {dac}')
dsbc=B.symmetric_difference(C)
print(f'diferencia simetrica B y C: {dsbc}')
ibc=B.intersection(C)
print(f'interseccion de B y C {ibc}')

print(f":{A} es subconjunto de B:{B} :{A.issubset(B)} {A<=B}")
print(f":{C} es subconjunto de A:{A} :{C.issubset(A)} {C<=A}")

print(f'100 esta en A{A}? : {100 in A}')
print(f'60 esta en A{A}, en B{B} y en C{C}? : {60  in A}: {60 in B}: {60 in C}')
print(f'900 no esta en C{C}?: {900 not in C}')