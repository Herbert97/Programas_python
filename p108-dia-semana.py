# Estacion del año
def diadelasemana(n):
    if n==1:
        dia='lunes'
    elif n==2:
        dia='martes'
    elif n==3:
        dia='miercoles'
    elif n==4:
        dia='jueves'
    elif n==5:
        dia='viernes'
    elif n==6:
        dia='sabado'
    elif n==7:
        dia='domingo'
    else:
        dia=''
    return dia


n = int(input('Dame un dia de la semana (1-7) ? '))
print(f'el dia es:  {diadelasemana(n)}')