# Tabla de multiplicar v2
import os
while(True):
    os.system('cls')
    t = int(input("Cual Tabla Quieres?"))
    n = int(input("Hasta donde ?"))
    c = 1
    while(c<=n):
        print("{0} x {1} = {2}".format(t,c,t*c))
        c+=1
    res=input("Deseas Continuar(S/N)?")
    if res.upper()=="N":
        break
print("Gracias ...")