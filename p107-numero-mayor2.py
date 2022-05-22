# numero mayor
def menor(c1,c2,c3):
    if c1<c2 and c1<c3:
        menor2 = c1
    elif c2<c1 and c2<c3:
        menor2 = c2
    else:
        menor2 = c3
    return menor2
   
    
print("Dame 3 calificaciones")
a,b,c = float(input()), float(input()), float(input())
print(f"la calificacion menor es: {menor(a,b,c)}")