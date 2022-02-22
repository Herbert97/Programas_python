# Tabla de multiplicar
import os
while(True):
    os.system('cls')
    t = int(input("cual Tabla ?"))
    c = 1
    while(c<=10):
        print("{0} x {1} = {2}".format(t,c,t*c))
        c+=1
    res=input("Deseas Continuar(S/N)?")
    if res.upper()=="N":
        break
print("Gracias ...")