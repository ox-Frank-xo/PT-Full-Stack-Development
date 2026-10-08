# 1. Crear un bucle For de Python

for i in range(5):
    print(i)



# 2. Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(a, b, c):
    return a + b + c

a = float(input("Ingrese el primer valor (a): "))
b = float(input("Ingrese el segundo valor (b): "))
c = float(input("Ingrese el tercer valor (c): "))

resultado = suma(a, b, c)
print(f"\nLa suma de {a} + {b} + {c} = {resultado}")



# 3. Función lambda

suma_lambda = lambda a, b, c: a + b + c

a = float(input("Ingrese el primer valor (a): "))
b = float(input("Ingrese el segundo valor (b): "))
c = float(input("Ingrese el tercer valor (c): "))

resultado = suma_lambda(a, b, c)
print(f"\nLa suma de {a} + {b} + {c} = {resultado}")



# 4. Verificar si 'nombre' está en 'lista_nombre'
nombre = 'Enrique'
lista_nombre = ('Jessica', 'Paul', 'George', 'Henry', 'Adán')

if nombre in lista_nombre:
    print(f"{nombre} coincide con un valor de la lista.")
else:
    print(f"{nombre} NO coincide con ningún valor de la lista.")

encontrado = False
for n in lista_nombre:
    if n == nombre:
        encontrado = True
        break

print("Coincidencia encontrada" if encontrado else "No se encontró coincidencia")