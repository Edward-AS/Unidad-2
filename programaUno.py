## 25-09-2024 ##

alumnos = ["Juan", "Pedro", "Luis", 10]

print(alumnos)
#print(alumnos[0])
#print(alumnos[1])
#print(alumnos[2])
#print(alumnos[-1])
#print(alumnos[-2])
#print(alumnos[-3])
#print(alumnos[-4])

#*Un arreglo mixto o combinado, es cuando este presenta diferentes tipos de datos
"""
print("Recorriendo elementos:")
for i in alumnos: #Recorriendo los elementos del arreglo
    print(i)

print("Recorriendo índices:")
for i in range(len(alumnos)): #Recorriendo los índices
    print(alumnos[i])

print("Recorriendo con while y los índices:")
indice = 0
while indice < len(alumnos):
    print(alumnos[indice])
    indice += 1
"""
"""
print("\nAgregar valores al arreglo:")

numeros = []

numeros.append(3)
numeros.append(5)
numeros.append(8)
print(numeros)


print("\nQuitar valores del arreglo (pop):")

numeros.pop()
print(numeros)


print("\nQuitar valores del arreglo (remove):")

alumnos.remove("Juan")
print(alumnos)
"""

n = "Luis"
print(f"\nIndice de {n}:")
i = alumnos.index(n)
print(i)

alumnos.pop(i)
print(f"\nLista sin {n}:")
print(alumnos)