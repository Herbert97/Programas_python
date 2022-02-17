# Calcular la paga de un trabajador, las horas extra se pagan al doble (>40)
print('Calculando la paga de horas extra de un trabajador (se pagan al doble)..')
nombre = input('Dame tu nombre > ')
horas = int(input('Horas trabajadas > '))
paga = float(input('Paga por hora > '))
if horas < 40 :
     total = horas * paga
   
else :
    extra = horas - 40
    total = (40 * paga ) + ( extra * (paga + paga))
print(f'\n{nombre} trabajo {horas} horas, con una paga de {paga}, total de pago {total}')