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