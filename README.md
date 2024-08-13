# Taller 2
### Equipo y Logo: Pantalla Azul

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
def separar_entero(parte_entera : float, digitos_entero : list) -> list:
    """
    Esta función separa los dígitos de una parte entera de un 
    número flotante y los almacena en una lista.
    
    Args:
        parte_entera (float): Representa la parte entera de un número 
        de punto flotante. 

        digitos_entero (list): Es una lista que almacenará los dígitos
        individuales de la parte entera de un número. 
    
    Returns:
    Se devuelve una lista que contiene los dígitos de la entrada 
    `parte_entera` (que es un flotante que representa la parte entera 
    de un número). 
    """

    if parte_entera < 0:
        # Se convierte la parte entera en un número positivo
        parte_entera = parte_entera * -1
    
        while parte_entera > 0:
            # Se extrae el entero más grande de la variable
            digito = int(parte_entera % 10)

            # Se añade el entero al primer puesto de la lista
            digitos_entero.insert(0, digito)

            # Se actualiza el valor de la variable 
            parte_entera //= 10

    else:
        while parte_entera > 0:
            # Se extrae el entero más grande de la variable
            digito = int(parte_entera % 10)

            # Se añade el entero al primer puesto de la lista
            digitos_entero.insert(0, digito)

            # Se actualiza el valor de la variable 
            parte_entera //= 10

    return digitos_entero

def separar_decimas(parte_decimal : float, digitos_decimal : list, 
                    presicion : int) -> list:
    """
    La función toma una parte decimal, una lista para almacenar los dígitos 
    decimales y un valor de precisión, y separa la parte decimal en dígitos 
    individuales.
    
    Args:
        parte_decimal (float): Representa la parte decimal de un número. 

        digitos_decimal (list): Es una lista que almacenará los dígitos
        individuales de la parte decimal de un número. 

        presicion (int): Es un número entero que representa el número de 
        decimales a considerar al extraer la parte decimal del input 
        `parte_decimal`. 

    Returns:
    Se devuelve una lista que contiene los dígitos individuales de la parte
    decimal de un número determinado. 
    """

    if parte_decimal < 0:
        # Se convierte la parte decimal en un número positivo
        parte_decimal = parte_decimal * -1

        while parte_decimal > 0:
            # Se extrae el decimal más grande de la variable
            digito = int(parte_decimal * 10 // 1)

            # Se añade el decimal a la lista
            digitos_decimal.append(digito)  

            # Se actualiza el valor de la variable 
            parte_decimal = float(f"{parte_decimal * 10 % 1:.{presicion}f}")

    else:
        while parte_decimal > 0:
            # Se extrae el decimal más grande de la variable
            digito = int(parte_decimal * 10 // 1)

            # Se añade el decimal a la lista
            digitos_decimal.append(digito)  
            
            # Se actualiza el valor de la variable 
            parte_decimal = float(f"{parte_decimal * 10 % 1:.{presicion}f}")

    return digitos_decimal
``` 
2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
 ```python
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

```    
4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **nota:** use *math* para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$
 ```python
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

```   
6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. **Pista:** Maneje valores booleanos y utilice el operador *in*.
  ```python

```    
7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
  ```python

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

``` 
9. Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.
  ```python

``` 
10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser **retornada** por la función. Implemente la perspectiva de un *patrón de acumulación* y también de *comprensión de listas*. **Desafío:** Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). **Pista:** Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?
 ```python
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
    print(f"Lista con los números ingresados múltiplos de 3: {lista_multiplos}")

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
print(f"Lista con los números ingresados múltiplos de 3: {lista_multiplos}"
```
### Bono
11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
 ```python
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
    
    # Se concatenan las listas de la matriz
    elementos = list(chain(*matriz))
    
    # Se comprueba si hay elementos repetidos en la matriz   
    if len(set(elementos)) != len(elementos):

        # Si hay elementos repetidos se retorna mensaje 
        print("La matriz tiene elementos repetidos")

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


