### 27-09-2024 ###

alumnos = ["Juan", "Pedro", "Luis", 10]

print("Buscar con 'for':")
for i in range(len(alumnos)):
    if alumnos[i] == "Luis":
        print(f"Si existe Luis en la lista, en la posición: {i + 1}")

print("\nBuscar con una función:")
if "Luis" in alumnos:
    print("Si existe Luis en la lista")
else:
    print("No existe Luis en la lista")

print("\nBuscar la posición:")
indice = alumnos.index("Luis")
print(f"La posición de Luis es: {indice + 1}")

print("\nBuscar la posición con try y except:")
try:
    indice = alumnos.index("Louis")
    print(f"La posición de Louis es: {indice + 1}")
except ValueError:
    print("No existe Louis en la lista")
