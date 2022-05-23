# muestra estadisticas de poblacion por año de 5 paises.
from p118modulopoblacion import*
poblacion=[
    {'pais':'Colombia','2018':49661, '2019':50339,'2020':50883,'2021':51266,},
    {'pais':'El Salvador','2018':6421, '2019':6454,'2020':6486,'2021':6518,},
    {'pais':'Mexico','2018':126191, '2019':127576,'2020':128933,'2021':130262,},
    {'pais':'Panama','2018':4177, '2019':4246,'2020':4315,'2021':4382,},
    {'pais':'Uruguay','2018':3449, '2019':3462,'2020':3474,'2021':3485,}
]

# Programa principal
print('\nPor nombres de menor a mayor: \n')
imprime(poblacion,'pais',False)
print('\nPais poblacion  del mayor a menor')
imprime(poblacion,'2020',True)

# mayor y menor 
may = valor_mayor(poblacion,'2018')
men = valor_menor(poblacion,'2018')
print('\n Pais  con mayor poblacion 2018: \n')
imprime(may,'',False)
print('\nPais  con menor poblacion 2018: \n')
imprime(men,'',False)

may = valor_mayor(poblacion,'2021')
men = valor_menor(poblacion,'2021')
print('\n Pais  con mayor poblacion 2021: \n')
imprime(may,'',False)
print('\nPais  con menor poblacion 2021: \n')
imprime(men,'',False)

