# Acceder a los elementos de una lista
nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]
print(f'todos los números : {nums}')
print(f'cuantos números son : {len(nums)}')
print(f'primero y último : {nums[0]}, {nums[-1]}')
print(f'del 2 al 6 : {nums[2:6]}')
print(f'los primeros 3 : {nums[:3]}')
print(f'los últimos 3 : {nums[6:]}')
print(f'3 antes del último : {nums[-4:-1]}')