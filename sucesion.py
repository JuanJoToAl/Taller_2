# Importamos módulo scipy.special para cacular el factorial 2 * i
from scipy.special import factorial

def calcular_sucesion(suma_aprox: float, termino: int, 
                     variable: float, resultado: float)  -> tuple:
    """ 
    Retorna el valor de la sumatoria hasta el término ingresado 
    por el usuario, la diferencia con el valor real de la función 
    coseno y el porcentaje de error de la aproximación. 
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
