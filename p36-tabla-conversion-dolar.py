# Tabla de conversion a dolar
tc = 20.71
pi = float(input("Valor inicial: "))
pf = float(input("Valor final : "))
c = pi
print("\nPesos\tDollar")
print("-"*15)
while c<=pf :
    print("{0}\t{1:.2f}".format(c,c/tc))
    c+=1
print("-"*15)