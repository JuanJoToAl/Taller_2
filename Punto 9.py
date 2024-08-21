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
