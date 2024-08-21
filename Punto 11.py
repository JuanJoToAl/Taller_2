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
