# Calcular la paga  de un trabajador
print("Calculando la paga de un trabajador")

# Entrada
nombre = input('nombre del trabajador')
horas  = int(input('Horas trabajadas'))
paga   = float(input('pago por hora?'))
tasa   = 0.3

# Proceso
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

# Salida
print('Resumen de pagos :')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una pago de {paga} pesos la hora, y una tasa de impuesto  {tasa}%')
print(f'Paga bruta :{pagabruta}')
print(f'Impuessto  :{impuesto}')
print(f'Paga neta  :{paganeta}')