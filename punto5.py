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