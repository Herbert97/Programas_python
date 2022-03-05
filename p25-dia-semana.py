# identificacion del dia de la semana segun un numero del 1-7 siendo 1 domingo y 7 viernes
numero=int(input('dame un numero entre el 1 y 7'))

if numero<=7:
    if numero== 1:
        print('el dia es domingo')
    elif numero== 2:
        print('el dia es lunes')
    elif numero== 3:
        print('el dia es martes')
    elif numero==4:
        print('el dia es miercoles')
    elif numero==5:
        print('el dia es jueves')
    elif numero==6:
        print('el dia es viernes')
    elif numero==7:
        print('el dia es sabado')
else:
    print('pilluelo ingresaste un numero fuera del rango dia incorrecto')
