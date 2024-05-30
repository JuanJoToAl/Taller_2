# Importamos módulo scipy.special para cacular factorial de 2 * termino
from scipy.special import factorial

def error_sucesion(suma_aprox: float, termino: int, variable: float, resultado: float) -> float:
    """
    La función calcula el valor aproximado del coseno utilizando una 
    suma y devuelve la suma, la diferencia con el valor real y el error 
    porcentual relativo.
    
    Args:
        suma_aprox (float): Representa la aproximación actual de la suma en el
        cálculo de su secuencia. 
        
        termino (int): Representa el número del término en una serie o 
        secuencia.

        variable (float): Representa el valor de entrada para el cual estás 
        calculando la aproximación del coseno. 

        resultado (float): Representa el valor real o verdadero de la expresión 
        o secuencia matemática que estás intentando aproximar. 
    
    Returns:
        Se devuelve la sumatoria, la diferencia entre el valor real de la 
        función y la aproximación y el error.
    """

    # Se calcula el coseno aproximado usando asignación con suma
    suma_aprox += ((-1) ** termino * (variable) ** (2 * termino) 
                   / factorial(2 * int(termino)))
    
    # Diferencia entre valor real y aproximación
    diferencia = resultado - suma_aprox

    # Error porcentual relativo
    error = abs(diferencia / resultado) * 100

    return suma_aprox, diferencia, error, 
