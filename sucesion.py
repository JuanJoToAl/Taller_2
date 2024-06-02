# Importamos módulo scipy.special para cacular el factorial 2 * i
from scipy.special import factorial

def calcular_sucesion(suma_aprox: float, termino: int, 
                     variable: float, resultado: float)  -> tuple:
    """
    La función calcula una aproximación del coseno de un número 
    utilizando la serie de Taylor hasta un término especificado.

    Args:
        suma_aprox (float): Representa la suma acumulada de la serie de Taylor. 

        termino (int): Representa el número máximo de términos a utilizar 
        en la serie de Taylor.

        variable (float): Variable para la cual se calcula el coseno 
        aproximado.

        resultado (float): Representa el valor real del coseno de `variable`. 
        Se utiliza para calcular el error porcentual relativo.

    Returns:
    Tupla con los siguientes valores:
        `suma_aprox`: Aproximación del coseno de `variable` hasta el término
        `termino`.
        
        `diferencia`: Diferencia entre el valor real (`resultado`) y la
        aproximación (`suma_aprox`).
        
        `error`: Error porcentual relativo entre el valor real y la
        aproximación.
        
        `termino`: Número de términos utilizados en la serie de Taylor.
    """
    
    # Se calcula el coseno aproximado hasta el térnimo dado mediante for
    for i in range(int(termino + 1)):
        suma_aprox += ((-1) ** i * (variable ** (2 * i)) 
                       / factorial(2 * i))
    # Diferencia entre valor real y aproximación
    diferencia = resultado - suma_aprox
    # Error porcentual relativo
    error = abs(diferencia / resultado) * 100
    return suma_aprox, diferencia, error, termino
