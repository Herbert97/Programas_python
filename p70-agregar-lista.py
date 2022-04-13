# Agregar elementos a la lista
nums = [80.3, 12.5, 60.2, 30.4]
print(f'todos los números : {nums}')
nums.append(90); nums.append(100)
print(f'agregar 90 y 100 al final : {nums}')
nums.insert(4,80)
print(f'insertar 80 en [4] : {nums}')
otros = [110,120,130]
nums.extend(otros)
print(f'extender con 110,120,130 : {nums}')