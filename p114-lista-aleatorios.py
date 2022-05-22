#generar dos listas con numeros aleatorios y sumarlas
import random
import os
MAX = 20

def genera_aleatorios():
    nums = []
    for i in range(MAX):
        nums.append( random.randint(1,100))
    return nums

def suma_listas(num1, num2):
    suma = []
    for i in range(MAX):
        suma.append( nums1[i] + nums2[i] )
    return suma

nums1 = genera_aleatorios()
nums2 = genera_aleatorios()
suma = suma_listas(nums1, nums2)

# programa principal
os.system('clear')
print(f'Lista 1 : {nums1}')
print(f'Lista 2 : {nums2}')
print(f'Suma listas : {suma}')