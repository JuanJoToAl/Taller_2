1.
#Se toma el número
numero=int(input("Ingrese el número "))
#Se determina una variable ´base´que nos ayudará a determinar cuántos dígitos tendrá el número
base=10
#Se crea una lista para añadir los dígitos
lista=[]
#Para simplificar, se imprime el número directamente si es menor a 10
if base>numero:
    lista.append(numero)
    print("El dígito del número es "+str(lista))
#Si no es de un dígito, se multiplica la base por 10 hasta que sea igual o mayor a el número inscrito
else:
    while base<=numero:
          base=base*10
#Ahora, se divide el número en la base exactamente, se añade el número a la lista, se le quita el dígito al número y se divide en 10 la base, hasta que la base llegue a 1, lo que significa que es el último dígito
    while base>=1:
          dig=numero//base
          lista.append(dig)
          numero=numero-(dig*base)
          base=base/10
#De esta manera, siempre da un 0 como primer dígito, entonces se elimina de la lista antes de imprimirla
    lista.pop(0)
    print("Los dígitos del número son:")
    print(lista)

2.

