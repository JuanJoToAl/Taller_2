# Punto 3
# Se piden los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Se hace una lista con los dígitos de cada número
lista1 = []
lista2 = []

# Para ahorrar tiempo, si los números son de 1 dígito y son iguales, significa que son espejo
if numero1 == numero2 and numero1 < 10:
    print("Los números son espejos")
else:
    # Determinación de la base
    base1 = 10
    base2 = 10

    # Se llenan las listas con los dígitos de cada número
    while base1 <= numero1:
        base1 *= 10
    while base1 > 1:
        base1 //= 10  # Corrección: usar división entera
        dig1 = numero1 // base1
        lista1.append(dig1)
        numero1 -= dig1 * base1

    while base2 <= numero2:
        base2 *= 10
    while base2 > 1:
        base2 //= 10  # Corrección: usar división entera
        dig2 = numero2 // base2
        lista2.append(dig2)
        numero2 -= dig2 * base2

    # Los números espejo deben tener la misma cantidad de dígitos, así que se descartan si las listas tienen diferente longitud
    if len(lista1) != len(lista2):
        print("Los números no son espejos")
    else:
        # Se crean variables para comparar los dígitos
        ayuda = 0
        elementos = len(lista2) - 1

        # Comparar los dígitos de los números
        while ayuda < len(lista1):
            if lista1[ayuda] != lista2[elementos]:
                print("Los números no son espejos")
                break
            ayuda += 1
            elementos -= 1

        # Si se recorren todos los dígitos y son iguales, los números son espejos
        if ayuda == len(lista1):
            print("Los números son espejos")
