# Punto 7
# Se crean dos listas, la primera tendrá todos los elementos y la segunda los elementos con vocales
lista1 = []
lista2 = []

# Se piden los elementos de la lista
a = input("Ingrese los elementos de la lista, si no quiere más elementos, escriba 'parar': ")

# Si no se escribe 'parar', el sistema seguirá añadiendo elementos
while a != "parar":
    lista1.append(a)
    a = input("Ingrese los elementos de la lista, si no quiere más elementos, escriba 'parar': ")

# Se recorren los elementos de la lista
for c in lista1:
    # Contador de vocales
    b = 0
    # Se cuenta el número de vocales en la cadena 'c'
    for char in c:
        if char in "aeiouAEIOU":
            b += 1
        # Si ya hay 2 o más vocales, se puede detener el conteo
        if b >= 2:
            lista2.append(c)
            break

# Se imprime la lista de elementos con 2 o más vocales, o un mensaje si no hay ninguno
if lista2:
    print("Los elementos con 2 o más vocales son: " + str(lista2))
else:
    print("No existe")