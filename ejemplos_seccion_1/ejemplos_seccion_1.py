# Ejemplos sección 1 

# Punto N° 1

print("Salidas punto N° 1")

lista = [1, 2, 3, 4, 5]

conjunto = {1, 2, 3, 4, 4, 5}

print(lista)
print(conjunto) # Elimina el duplicado en el conjunto

# Acceso a la lista
print("El elemento en la lista[2]: ", lista[2])

# print(conjunto[2]) # Esto genera un error 

conjunto_2 = {3, 4, 5, 6, 7}

# Operaciones en los conjuntos

print("Unión de conjuntos:", conjunto | conjunto_2)
print("Intersección de conjuntos:", conjunto & conjunto_2)


# Punto N° 2

# Función que devuelve números pares hasta un limite bajo demanada

print("Salidas punto N° 2")

def num_pares(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2
        
pares = num_pares(10)
print(next(pares)) # devuelve el # 0
print(next(pares)) # devuelve el # 2
print(next(pares)) # devuelve el # 4
print(next(pares)) # devuelve el # 6


# Punto N° 3

# Usando listas y diccionarios nativos de Python
# Es ineficiente para calcular de manera rápida el promedio de salarios

datos = [
    {"nombre": "Ana", "edad": 25, "salario": 3000},
    {"nombre": "Carlos", "edad": 30, "salario": 4000},
    {"nombre": "Elena", "edad": 35, "salario": 5000}
]

# Obtener los salarios manualmente y calcular el promedio de estos
salarios = [persona["salario"] for persona in datos]
promedio = sum(salarios) / len(salarios)
print(f"Salario promedio: {promedio}")

# Con Pandas se realiza de manera agil, eficiente y más claro

import pandas as pd

print("Salidas punto N° 3")

# Creamos un DataFrame
df = pd.DataFrame([
    {"nombre": "Ana", "edad": 25, "salario": 3000},
    {"nombre": "Carlos", "edad": 30, "salario": 4000},
    {"nombre": "Elena", "edad": 35, "salario": 5000}
])

# Calcular promedio de manera más clara y agil
promedio = df["salario"].mean()
print(f"Salario promedio: {promedio}")


# Punto N° 4

print("Salidas punto N° 4")

# Creamos un DataFrame
df = pd.DataFrame({
    "nombre": ["Ana", "Carlos", "Eliana"],
    "edad": [25, 30, 35]
    })

# Aplicamos una transformación con map()
df["edad_doble"] = df["edad"].map(lambda x: x * 2)

print(df)

# Aplicamos una transformación con apply()
df["edad_triple"] = df["edad"].apply(lambda x: x * 3)
