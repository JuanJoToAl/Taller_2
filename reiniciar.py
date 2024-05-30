def reiniciar_variable(suma_aprox : float, termino : float, error : float) -> tuple:
    """
    La función restablece los valores de `suma_aprox`, `termino` y `error` 
    a valores iniciales específicos y los devuelve como una tupla.
    
    Args:
        suma_aprox (float): Representa la suma aproximada de la serie o
        cálculo.

        termino (float): El parámetro `termino` en la función `reiniciar_variable` representa un valor
        flotante que se usa como variable dentro de la función. En este contexto, se restablece a un valor
        de -1 cuando se llama a la función.

        error (float): El parámetro `error` en la función `reiniciar_variable` parece representar el valor
        de error asociado con algún cálculo o proceso. En la función, la variable `error` se establece en
        `Ninguno` cuando se llama a la función para restablecer o reiniciar ciertas variables (`suma_aprox`,
        `termin
    
    Returns:
      La función `reiniciar_variable` devuelve una tupla que contiene los valores de `suma_aprox`,
    `termino` y `error` después de que se hayan restablecido a valores específicos. Los valores que se
    devuelven son "0" para "suma_aprox", "-1" para "termino" y "Ninguno" para "error".
    """

    # Se reinician las variables
    suma_aprox = 0
    termino = -1
    error = None
    return suma_aprox, termino, error