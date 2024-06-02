def reiniciar_variable(suma_aprox : float, termino : float, error : float) -> tuple:
    """
    Esta función reinicia los valores de tres variables: 
    `suma_aprox`, `termino` y `error`.

    Args:
      suma_aprox (float): Representa la suma aproximada de 
      la serie de Taylor.
      
      termino (float): Representa el último término calculado 
      en la serie de Taylor.
      
      error (float): Representa el error relativo de la aproximación 
      con la serie de Taylor.
      
    Returns:
      Tupla con las tres variables reiniciadas: 
      `(suma_aprox, termino, error)`.
    """

    # Se reinician las variables
    suma_aprox = 0
    termino = -1
    error = None
    
    return suma_aprox, termino, error