# Taller 2
### Equipo y Logo: Pantalla Azul :/

<div align='center'>
<figure> <img src="https://github.com/J0s3ph2705/Taller-pdc_8/assets/159032718/b0dd65be-48ba-400b-a302-63eb8381cf65" alt="" width="1000" height="auto"/></br>
</figure>

</div> 

### Integrantes:

1. Joseph Lievano (1052383083)
2. Juan José	Tobar Álvarez (1112042373)

# Taller

1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. **Pista:** Utilice los operadores módulo (%) y división entera (//).
  ```python
# Punto 1
def digitos_numero(numero : int) -> None:
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
    return None
if __name__ == "__main__":
    #Se toma el número
    numero=int(input("Ingrese el número "))
    digitos_numero(numero)
``` 

2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
 ```python
# Punto 2
# Se importan módulos para calcular los dígitos de los números
from digitos import *

# Se declaran variables
parte_entera : int
parte_entera_negativa : int
parte_decimal : float
parte_decimal_negativa : float
presicion : int

# Se declaran e inicializan listas
digitos_entero : list = []
digitos_entero_negativo : list = []
digitos_decimal : list = []
digitos_decimal_negativo : list = []

try:
    if __name__ == "__main__":
        # Solicitud: número a separar
        flotante = float(input("Ingrese un número real"))

        # Solicitud: presición de los decimales
        presicion = int(input("Ingrese la cantidad de decimales de presición"))

        if flotante < 0:
            # Calculo de parte entera de flotante negativo
            parte_entera = flotante // 1 + 1

            # Calculo de parte decimal de flotante negativo
            parte_decimal = float(f"{flotante % parte_entera:.{presicion}f}")

            # Se llaman las funciones para calcular los dígitos
            digitos_entero = separar_entero(parte_entera, digitos_entero ) 
            digitos_decimal = separar_decimas(parte_decimal, digitos_decimal, presicion) 
        
        elif flotante == 0:
            parte_entera = 0
            parte_decimal = 0

            # Se añade el 0 a la lista
            digitos_entero.append(flotante)

            # Se añade la cantidad de 0's que solicite el usuario 
            digitos_decimal = digitos_entero * presicion
            
        else: 
            # Calculo de parte entera de flotante
            parte_entera = flotante // 1

            # Calculo de parte decimal de flotante 
            parte_decimal = float(f"{flotante % parte_entera:.{presicion}f}")

            # Se llaman las funciones para calcular los dígitos
            digitos_entero = separar_entero(parte_entera, digitos_entero ) 
            digitos_decimal = separar_decimas(parte_decimal, digitos_decimal, presicion) 

        # Se imprime la parte entera y decimal del número
        print(f"La parte entera del número es: {int(parte_entera)}")
        print(f"La parte decimal del número es: {parte_decimal:.{presicion}f}")
        
        # Se imprimen los dígitos de la parte entera y decimal
        print(f"Los dígitos de la parte entera son: {digitos_entero}")
        print(f"Los dígitos de la parte decimal son:: {digitos_decimal}")

except ValueError:
    print("Entrada inválida, por favor intente de nuevo")
```    

3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

 ```python
# Punto 3

def numeros_espejo(numero1 : int, numero2 : int) -> None:
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

if __name__ == "__main__":
    # Se piden los números
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numeros_espejo(numero1, numero2)
```

4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **nota:** use *math* para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$

 ```python
# Punto 4
# Importamos módulo math para cacular valor real de coseno
import math

# Importamos sucesion y error para calcular coseno con serie de Taylor
from sucesion import calcular_sucesion
from error import error_sucesion

# Importamos reiniciar para "vaciar" variables
from reiniciar import reiniciar_variable

# Variable: suma de la serie de Taylor
suma_aprox: float = 0

try:
    if __name__ == "__main__":
        # Solicitud: valor de la variable
        variable = float(input("Ingrese valor variable para evaluar ceno: "))

        # Solicitud: número del término inicial
        termino = int(input("Ingrese la cantidad de terminos a utilizar de la serie"))  

        # Función coseno evaluada en la variable
        resultado = math.cos(variable)

        # Se llama calculan diferentes valores relacionados a la sucesion
        suma_aprox, diferencia, error, termino = calcular_sucesion(suma_aprox, termino, 
                                                                   variable, resultado)

        # Impresión: valor aproximado
        print(f"Valor aprox. función en término ({termino}): {suma_aprox}")

        # Impresión: valor real
        print(f"Valor real función: {resultado}")

        # Impresión: diferencia absoluta
        print(f"Diferencia absoluta entre valor real y aprox.: {abs(diferencia)}")

        # Se reinician las variables
        suma_aprox, termino, error = reiniciar_variable(suma_aprox, termino, error)

        # Bucle: iteración hasta error < 10%
        while error is None or error >= 10:
            termino += 1
            suma_aprox, diferencia, error = error_sucesion(suma_aprox, termino, 
                                                           variable, resultado)
            
        # Impresión: términos para error < 10%
        print(f"Se obtiene menos del 10% error con {termino} términos.")

        # Se reinician las variables
        suma_aprox, termino, error = reiniciar_variable(suma_aprox, termino, error) 

        # Bucle: iteración hasta error < 1%
        while error is None or error >= 1:
            termino += 1
            suma_aprox, diferencia, error = error_sucesion(suma_aprox, termino, 
                                                           variable, resultado)
            
        # Impresión: términos para error < 1%
        print(f"Se obtiene menos del 1% error con {termino} términos.")

        # Se reinician las variables
        suma_aprox, termino, error = reiniciar_variable(suma_aprox, termino, error)

        # Bucle: iteración hasta error < 0.1%
        while error is None or error >= 0.1:
            termino += 1
            suma_aprox, diferencia, error = error_sucesion(suma_aprox, termino, 
                                                           variable, resultado)
            
        # Impresión: términos para error < 0.1%
        print(f"Se obtiene menos del 0.1% error con {termino} términos.")

        # Se reinician las variables
        suma_aprox, termino, error = reiniciar_variable(suma_aprox, termino, error)

        # Bucle: iteración hasta error < 0.001%
        while error is None or error >= 0.001:
            termino += 1
            suma_aprox, diferencia, error = error_sucesion(suma_aprox, termino, 
                                                           variable, resultado)
            
        # Impresión: términos para error < 0.001%
        print(f"Se obtiene menos del 0.001% error con {termino} términos.")

except ValueError:
    print("Entrada inválida, por favor intente de nuevo")
``` 

5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. **Pista:** Puede ser de utilidad chequear el [Algoritmo de Euclides](https://es.wikipedia.org/wiki/Algoritmo_de_Euclides) para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.

 ```python
# Punto 5
#Se piden los números
numero1=int(input("Ingrese el primer número "))
numero2=int(input("Ingrese el segundo número "))
#Esta solución usa reiteración y recurción, así que se hacen las funciones
def mcd1(numero1,numero2):
    return numero1/numero2
def mcd2(numero1,numero2):
    return numero2/numero2
#Luego se desarrolla el algoritmo de Euclides, tomando en cuenta cuál número es mayor
if numero1>numero2:
#Se llama la función
    a=mcd1(numero1,numero2)
    b=numero1//numero2
#Se compara la división normal con la división exacta para saber si queda residuo o no
    while a!=b:
#Luego se reemplazan valores para seguir con el algoritmo hasta que no qude residuo
        numero1=numero2
        numero2=(a-b)*numero2
        a=numero1/numero2
        b=numero1//numero2
#Cuando no se halla residuo, se imprime el resultado
    print("El máximo común divisor de los números es "+str(numero2))
#Se repite el proceso para cuando l segundo número es mayos que el primero
else:
    a=mcd2(numero2,numero1)
    b=numero2//numero1
    while a!=b:
        numero2=numero1
        numero1=(b-a)*numero1
        a=numero2/numero1
        b=numero2//numero1
    print("El máximo común divisor de los números es "+str(numero1))

#Posdata: El mínimo común múltiplo de 2 números siempre va a ser divisible exactamente entre el máximo común divisor
```

6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. **Pista:** Maneje valores booleanos y utilice el operador *in*.

  ```python
# Punto 6

def encontrar_numeros_repetidos():
    """
    Encuentra y muestra números repetidos introducidos por el usuario.

    Args:
        None

    Returns:
        None

    El usuario introduce números repetidamente hasta que escribe 'fin'.
    La función muestra la lista completa de números y los números repetidos
    junto con su frecuencia.
    """
    
    # Lista para almacenar los números introducidos por el usuario
    numeros_repetidos = []
    
    # Diccionario para contar la frecuencia de cada número
    frecuencia_numeros = {}
    
    # Bandera para controlar el bucle de entrada
    terminar_proceso = False
    
    # Bucle para solicitar números hasta que el usuario decida terminar
    while not terminar_proceso:
        
        # Solicita al usuario un número o 'fin' para terminar
        inicio = input("Escriba un número o 'fin' para terminar y mostrar los números repetidos: ")
        
        # Verifica si el usuario desea terminar el proceso
        if inicio.lower() == 'fin':
            terminar_proceso = True
        else:
            try:
                # Intenta convertir la entrada a un número flotante
                n = float(inicio)
                
                # Agrega el número a la lista de números
                numeros_repetidos.append(n)
                
                # Actualiza la frecuencia del número en el diccionario
                if n in frecuencia_numeros:
                    frecuencia_numeros[n] += 1
                else:
                    frecuencia_numeros[n] = 1
            except ValueError:
                # Informa al usuario si la entrada no es un número válido
                print("Por favor, escriba un número válido.")
    
    # Muestra la lista completa de números introducidos
    print(f"La lista de números es: {numeros_repetidos}")
    
    # Muestra los números repetidos y su frecuencia
    print("Números repetidos: ")
    for numero, frecuencia in frecuencia_numeros.items():
        if frecuencia > 1:
            # Imprime el número y la cantidad de veces que se repite
            print(f"{numero} se repite {frecuencia} veces")

# Ejecuta la función si el script es ejecutado directamente
if __name__ == "__main__":
    encontrar_numeros_repetidos()
```

7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

  ```python
# Punto 7
def llenar_lista() -> list:
    # Se crean dos listas, la primera tendrá todos los elementos y la segunda los
    # elementos con vocales
    lista1 = []

    # Se piden los elementos de la lista
    a = input("Ingrese los elementos de la lista, si no quiere más elementos, escriba 'parar': ")

    # Si no se escribe 'parar', el sistema seguirá añadiendo elementos
    while a != "parar":
        lista1.append(a)
        a = input("Ingrese los elementos de la lista, si no quiere más elementos, escriba 'parar': ")

    return lista1

def mensaje_en_lista(lista1 : list) -> None:
    lista2 = []
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

    # Se imprime la lista de elementos con 2 o más vocales, o un mensaje si no hay
    # ninguno
    if lista2:
        print("Los elementos con 2 o más vocales son: " + str(lista2))
    else:
        print("No existe")
    
    return None

if __name__ == "__main__":
    lista1 = llenar_lista()
    mensaje_en_lista(lista1)
```

8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. **Ejemplo:**
<center>
<table border="1">
<tr>
<td>
lista1: [1, 'Hola', -12.3 ,True]<br>
lista2: [11, -12.3, 'Hola', False]
</td>
</tr>
<tr>
<td>
salida: [1, True]
</td>
</tr>
</table>
</center>

 ```python
# Punto 8

def encontrar_diferencia_entre_listas():
    """
    Encuentra los elementos que están en la primera lista pero no en la
    segunda.
   
    Args:
        None

    Returns:
        None

    Solicita al usuario que introduzca dos listas de elementos separados por
    comas, y muestra los elementos que están en la primera lista y no en la
    segunda.
    """
    diferencia = []  # Lista para almacenar los elementos únicos de lista1
    
    # Solicita al usuario elementos de primera lista y los convierte en lista

    lista1 = input("Escribe los elementos de la primera lista separados por comas: ").split(',')
   
    # Solicita al usuario elementos de segunda lista y los convierte en lista
    lista2 = input("Escribe los elementos de la segunda lista separados por comas: ").split(',')
   
    # Elimina espacios en blanco alrededor de cada elemento en ambas listas
    lista1 = [elemento.strip() for elemento in lista1]
    lista2 = [elemento.strip() for elemento in lista2]
   
    # Muestra los elementos de la primera lista
    print(f"Elementos de la primera lista: {lista1}")
   
    # Muestra los elementos de la segunda lista
    print(f"Elementos de la segunda lista: {lista2}")
   
    # Encuentra elementos que están en primera lista pero no en segunda
    diferencia = [elemento for elemento in lista1 if elemento not in lista2]
   
    # Muestra los elementos que están en primera lista y no segunda
    print(f"Los elementos que tiene la primera lista y que no tiene la segunda son: {diferencia}")

# Ejecuta la función si el script es ejecutado directamente
if __name__ == "__main__":
    encontrar_diferencia_entre_listas()
```

9. Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.
   
  ```python
# Punto 9

def analizar_numeros():
    """
    Analiza una lista de números introducidos por el usuario, calculando
    diversas métricas estadísticas y mostrando los resultados.
    
    Args:
        None

    Returns:
        None

    La función solicita cinco números al usuario, calcula y muestra el
    promedio, la mediana, el promedio multiplicativo, ordena los números
    en forma ascendente y descendente, y realiza cálculos adicionales.
    """
    
    n = []  # Lista para almacenar los números introducidos por el usuario

    # Solicita al usuario cinco números y los agrega a la lista n
    for num in range(5):
        num = float(input("Escribe un numero: "))
        n.append(num)
    
    def Cal_promedio(n):
        """
        Calcula el promedio de una lista de números.

        Args:
            n (list of float): Lista de números.

        Returns:
            float: Promedio de los números en la lista.
        """
        return sum(n) / len(n)
    
    def cal_mediana(n):
        """
        Calcula la mediana de una lista de números.

        Args:
            n (list of float): Lista de números.

        Returns:
            float: Mediana de los números en la lista.
        """
        num_ordenados = sorted(n)  # Ordena la lista de números
        n = len(num_ordenados)
        if n % 2 == 0:
            # Calcula la mediana para una lista de longitud par
            return (num_ordenados[n // 2 - 1] + num_ordenados[n // 2]) / 2
        else:
            # Calcula la mediana para una lista de longitud impar
            return num_ordenados[n // 2]
    
    def cal_promedio_multiplicativo(n):
        """
        Calcula el promedio multiplicativo de una lista de números.

        Args:
            n (list of float): Lista de números.

        Returns:
            float: Promedio multiplicativo de los números en la lista.
        """
        prod = 1
        for num in n:
            prod *= num  # Multiplica todos los números
        return prod ** (1 / len(n))  # Calcula la raíz enésima del producto
    
    def orden_ascen(n):
        """
        Ordena la lista de números en orden ascendente.

        Args:
            n (list of float): Lista de números.

        Returns:
            list of float: Lista de números ordenada en forma ascendente.
        """
        return sorted(n)
    
    def ordenar_descen(n):
        """
        Ordena la lista de números en orden descendente.

        Args:
            n (list of float): Lista de números.

        Returns:
            list of float: Lista de números ordenada en forma descendente.
        """
        return sorted(n, reverse=True)
    
    def cal_potencia(n):
        """
        Calcula la potencia del mayor número elevado al menor número en la
        lista.

        Args:
            n (list of float): Lista de números.

        Returns:
            float: Potencia del mayor número elevado al menor número.
        """
        maximo = max(n)  # Encuentra el número máximo
        minimo = min(n)  # Encuentra el número mínimo
        return maximo ** minimo  # Calcula la potencia
    
    def cal_raiz_cubica_menor(n):
        """
        Calcula la raíz cúbica del menor número en la lista.

        Args:
            n (list of float): Lista de números.

        Returns:
            float: Raíz cúbica del menor número en la lista.
        """
        minimo = min(n)  # Encuentra el número mínimo
        return minimo ** (1/3)  # Calcula la raíz cúbica
    
    # Muestra los números introducidos por el usuario
    print(f"Los números escritos son: {n}")
    
    # Muestra el promedio de los números
    print(f"El promedio es: {Cal_promedio(n)}")
    
    # Muestra la mediana de los números
    print(f"La mediana es: {cal_mediana(n)}")
    
    # Muestra el promedio multiplicativo de los números
    print(f"El promedio multiplicativo es: {cal_promedio_multiplicativo(n)}")
    
    # Muestra los números en orden ascendente
    print(f"Los números en orden ascendente son: {orden_ascen(n)}")
    
    # Muestra los números en orden descendente
    print(f"Los números en orden descendente son: {ordenar_descen(n)}")
    
    # Muestra la potencia del mayor número elevado al menor número
    print(f"La potencia del mayor número elevado al menor número es: {cal_potencia(n)}")
    
    # Muestra la raíz cúbica del menor número
    print(f"La raíz cúbica del menor número es: {cal_raiz_cubica_menor(n)}")

# Ejecuta la función si el script es ejecutado directamente
if __name__ == "__main__":
    analizar_numeros()
```

10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser **retornada** por la función. Implemente la perspectiva de un *patrón de acumulación* y también de *comprensión de listas*. **Desafío:** Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). **Pista:** Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?
    
 ```python
# Punto 10
# Se declara e inicializa la lista
lista_numeros : list = []
# Se declaran la lista
lista_múltiplos : list 
# Se declaran e/o inicializan variables
numero : str
bandera : bool = True

def agregar_numeros(bandera, lista_numeros : list) -> list:
   """
   La función permite ingresa números enteros a una lista hasta que el 
   usuario ingrese la palabra "parar" (o "Parar") en minúscula.

   Args:
       lista_numeros (list): Lista donde se almacenarán los números 
       ingresados por el usuario. 

   Returns:
       Se retorna lista que contiene todos los números enteros 
       ingresados por el usuario. 
   """
   
   # Se agregan números a la lista hasta ingresar "parar" o "Parar"
   while bandera:
       numero = str(input("Ingrese números enteros o parar para deternerel ciclo"))
       if numero.lower() == "parar":
           bandera = False
       else:
           lista_numeros.append(int(numero))

   return lista_numeros

if __name__ == "__main__":

   lista_numeros = agregar_numeros(bandera, lista_numeros)
   # Se verifica cuáles números de la lista son múltiplos de 3
   lista_multiplos = [x for x in lista_numeros if x % 3 == 0]

   # Se imprime la lista con los números ingresados
   print(f"La lista con los números ingresados es: {lista_numeros}")
   
   # Se imprime la lista con los múltiplos de 3 de la lista "lista_numeros"
   print(f"Lista con los números ingresados múltiplos de 3 (usando el módulo): {lista_multiplos}")

#La manera sin ¨%¨

from digitos import *
# Se declara e inicializa la lista
lista_numeros : list = []

# Se declaran la lista
lista_multiplos : list 

# Se declaran e/o inicializan variables
numero : str
bandera : bool = True

def agregar_numeros(bandera : bool, lista_numeros : list) -> list:
   """
   La función permite ingresar números enteros a una lista hasta 
   que el usuario ingrese la palabra "parar" (o "Parar") en minúscula.

   Args:
       bandera (bool): Controla la ejecución del bucle `while`. 
       
       lista_numeros (list): Almacena los números ingresados por el usuario. 

   Returns:
   Lista que contiene todos los números enteros ingresados por el usuario. 
   """

   # Se agregan enteros a la lista hasta ingresar "parar" o "Parar"
   while bandera:
       numero = str(input("Ingrese números enteros o parar para deternerel ciclo"))
       if numero.lower() == "parar":
           bandera = False
       else:
           lista_numeros.append(int(numero))
   
   return lista_numeros

def multiplos(lista_numeros : list) -> list:
   """ 
   La función identifica y filtra los números múltiplos 
   de 3 dentro de una lista.

   Args:
       lista_numeros (list): Lista que contiene números enteros.

   Returns:
       Lista que contiene solo los números múltiplos de 3 que se 
       encontraron en `lista_numeros`.
   """

   # Se elementos de "lista_numeros" y se agregan a "lista_multiplos" 
   lista_multiplos = [x for x in lista_numeros if sum(separar_entero(x, [])) 
                      // 3 * 3 == sum(separar_entero(x, []))]
   
   return lista_multiplos

if __name__ == "__main__":
   lista_numeros = agregar_numeros(bandera, lista_numeros)

   # Se verifica cuáles números de la lista son múltiplos de 3
   lista_multiplos = multiplos(lista_numeros) 

# Se imprime la lista con los números ingresados
print(f"La lista con los números ingresados es: {lista_numeros}")

# Se imprime la lista con los múltiplos de 3 de la lista "lista_numeros"
print(f"Lista con los números ingresados múltiplos de 3 (sin usar el módulo): {lista_multiplos}")
```

### Bono
11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que
    una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada
    una de sus columnas y de cada diagonal es igual.

 ```python
# Punto 11
# Se importa chain para comprobar si la matriz tiene elementos repetidos 
from itertools import chain

# Se declaran e/o inicializan variables
matriz : list = []
num_filas_columnas :int
filas : list = []
bandera : bool = True
elementos : list
suma_verificadora : float
suma_columnas : float
suma_diagonal_mayor : float
suma_diagonal_menor : float
indice : int

def llenar_matriz(matriz : list, num_filas_columnas : int, filas : list) -> list:
    """
    La función permite crear una matriz de tamaño especificado por el 
    usuario y llenarla con números ingresados por el usuario.

    Args:
        matriz (list): Representará la matriz final. 
        
        num_filas_columnas (int): Número que indica la cantidad de filas y
        columnas que tendrá la matriz.
        
        filas (list): Lista temporal que se utilizará para almacenar los
        números ingresados por el usuario para cada fila.
        
    Returns:
    Lista que representa la matriz final con las dimensiones y valores
    especificados por el usuario.
    """

    print(f"La matriz se ve de la siguiente forma:")
    # Se recorren la cantidad de filas ingresadas por el usuario
    for _ in range(num_filas_columnas): 

        # Se recorren la cantidad de columnas ingresadas por el usuario
        for _ in range(num_filas_columnas):

        # Se solicita al usuairo que ingrese los números van a ir en cada fila
            filas.append(float(input("Ingrese un número")))

        # Se añade la fila a la matriz
        matriz.append(filas) 

        # Se imprime la fila para ver como se va construyendo la matriz
        print(f"[{' '.join(map(str, filas))}]")

        # Se vacía la variable para llenarla con números de la siguiente fila
        filas = []  

    return matriz

def elementos_diferentes(matriz : list, bandera : bool) -> bool:
    """
    La función verifica si una matriz bidimensional contiene elementos 
    repetidos.

    Args:
        matriz (list): Representa la matriz bidimensional.

        bandera (bool): Controla la ejecución del bucle `while` en una función
        externa.
        
    Returns:
    Valor de tipo `bool`:
        * `True` si la matriz no contiene elementos repetidos.
        * `False` si la matriz contiene elementos repetidos.
    """
    
    elementos = []
    # Se concatenan las listas de la matriz
    for filas in matriz:
        elementos += filas

    # Se comprueba si hay elementos repetidos en la matriz   
    if len(set(elementos)) != len(elementos):

        # Si hay elementos repetidos se retorna mensaje 
        print("La matriz tiene elementos repetidos, no puede ser mágica")

        # Si hay elementos repetidos se detiene llamado de funciones
        return False
  
    return bandera

def suma_filas(matriz: list, bandera: bool) -> tuple:
    """
    Función que verifica si una matriz bidimensional es mágica.

    Parámetros:
        matriz (list): La matriz bidimensional a evaluar.

        bandera (bool): Bandera que indica si se debe imprimir un mensaje en
        caso de que la matriz no sea mágica.
        
    Retorno:
        tuple: Tupla que contiene:
            - Bandera que indica si la matriz es mágica (True) o no (False).
            - Suma de los elementos de la primera fila.
    """

    # Se suman los elementos de la primera fila
    suma_verificadora = sum(matriz[0])

    # Se recorren las filas restantes
    for i in range(1, len(matriz)):

        # Se verifica la constante mágica en todas las filas
        if suma_verificadora != sum(matriz[i]):

            # En caso de no cumplirse la condición se imprime el mensaje
            print("La matriz no es mágica")
            return False, suma_verificadora
 
    return bandera, suma_verificadora

def calcular_suma_columnas(matriz : list, bandera : bool, 
                           suma_verificadora : float) -> bool:
    """
    Función que calcula la suma de las columnas de una matriz bidimensional 
    y verifica si es mágica.
    
    Parámetros:
        matriz (list): La matriz bidimensional a evaluar.

        bandera (bool): Bandera que indica si se debe imprimir un mensaje en
        caso de que la matriz no sea mágica.
        
        suma_verificadora (float): Suma de los elementos de la primera fila,
        utilizada como constante mágica.
        
    Retorno:
        bandera (bool): Indica si la matriz es mágica (True) o no (False).
    """

    # Se recorren las columnas empezando por la primera
    for j in range(len(matriz[0])):

        # Se recorren y suman los elementos de las columnas 
        suma_columnas = sum(matriz[i][j] for i in range(len(matriz)))

        # Se verifica constante mágica en todas las columnas
        if suma_columnas != suma_verificadora:

        # En caso de no cumplirse la condición se imprime el mensaje
            print("La matriz no es mágica")
            return False
    
    return bandera

def diagonal_mayor(matriz: list, bandera : bool, 
                   suma_verificadora : float) -> bool:
    """
    Función que calcula la suma de la diagonal mayor de una matriz
    bidimensional y verifica si es mágica.
    
    Parámetros:
        matriz (list): La matriz bidimensional a evaluar.

        bandera (bool): Bandera que indica si se debe imprimir un mensaje en
        caso de que la matriz no sea mágica.
        
        suma_verificadora (float): Suma de los elementos de la primera fila,
        utilizada como constante mágica.
        
    Retorno:
        bandera (bool): indica si la matriz es mágica (True) o no (False).
    """

    # Se recorren elementos de la diagonal mayor.
    suma_diagonal_mayor = sum(matriz[i][i] for i in range(len(matriz)))

    # Se verifica constante mágica en la diagonal mayor
    if suma_verificadora != suma_diagonal_mayor:  

        # En caso de no cumplirse la condición se imprime el mensaje
        print("La matriz no es mágica")
        return False
    
    return bandera
  
def diagonal_menor(matriz: list, bandera : bool, 
                   suma_verificadora : float) -> bool:
    """
    Función que calcula la suma de la diagonal menor de una matriz
    bidimensional y verifica si es mágica.
    
    Parámetros:
        matriz (list): La matriz bidimensional a evaluar.

        bandera (bool): Bandera que indica si se debe imprimir un mensaje en
        caso de que la matriz no sea mágica.
        
        suma_verificadora (float): Suma de los elementos de la primera fila,
        utilizada como constante mágica.
        
    Retorno:
        bool: Bandera que indica si la matriz es mágica (True) o no (False).
    """

    # Varible para recorrer la diagonal menor empezando por la última fila
    indice = -1

    suma_diagonal_menor = 0.0
    # Se crea bucle para recorrer los elementos de la diagonal menor
    for j in range(len(matriz)):

        # Suma de elementos de diagonal menor y se guarda resultado en variable
        suma_diagonal_menor += matriz[indice][j]

        # Se actualiza variable para pasar a fila anterior
        indice -= 1

    # Se verifica constante mágica en la diagonal mayor
    if suma_verificadora != suma_diagonal_menor: 

        # En caso de no cumplirse la condición se imprime el mensaje 
        print("La matriz no es mágica")
        return False
    
    return bandera

if __name__ == "__main__":
    # Solicitud: número de filas y columnas de la matriz
    num_filas_columnas = int(input(
                                    "Ingrese el número de filas y columnas para la matriz"
                                    ))

    # Condicional para matrices de orden 2
    if num_filas_columnas == 2:
        print("No hay matrices mágicas de orden 2")

    # Condicional para input de matrices con orden negativo
    elif num_filas_columnas < 0:
        print("No puede haber una cantidad negativa de columnas o filas")

    # Condicional para input de matrices con orden cero
    elif num_filas_columnas == 0:
        print("Sin filas ni columnas no hay matriz :(")

    else:
        # Lamado de función para llenar matriz
        matriz = llenar_matriz(matriz, num_filas_columnas, filas)

        # Lamado de función para comprobar si hay elemtos repetidos
        bandera = elementos_diferentes(matriz, bandera)

        # Lamado a funciones si se cumplen las condiciones dentro de estas
        if bandera:
            print("La matriz no tiene elementos repetidos")
            bandera, suma_verificadora  = suma_filas(matriz, bandera)      
        
        if bandera:
            bandera = calcular_suma_columnas(matriz, bandera, suma_verificadora)

        if bandera:
            bandera = diagonal_mayor(matriz, bandera, suma_verificadora)
        
        if bandera:
            bandera = diagonal_menor(matriz, bandera, suma_verificadora)

        if bandera:
            # Si se cumplen todas las condiciones se imprimen mensajes finales
            print("La matriz es mágica")
            print(f"La constante mágica de la matriz es: {suma_verificadora}")
``` 
