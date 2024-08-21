#Se piden los números
numero1=int(input("Ingrese el primer número "))
numero2=int(input("Ingrese el segundo número "))
#Se hace lo mismo que en el punto uno: Se hace una lista con los dígitos de cada número con ayuda de un número base
base1=10
base2=10
lista1=[]
lista2=[]
#Para ahorrar tiempo, si los números son de 1 dígito y son iguales, significa que son espejo
if numero2==numero1 and numero1<10:
    print("Los números son espejos")
#Se llenan las listas con los dígitos de cada número
else:
    while base1<=numero1:
          base1=base1*10
    while base1>=1:
          dig1=numero1//base1
          lista1.append(dig1)
          numero1=numero1-(dig1*base1)
          base1=base1/10
    lista1.pop(0)
    while base2<=numero2:
          base2=base2*10
    while base2>=1:
          dig2=numero2//base2
          lista2.append(dig2)
          numero2=numero2-(dig2*base2)
          base2=base2/10
    lista2.pop(0)
#Se crean 2 variables que servirán como index, el primero empieza en 0 y va subiendo mientras que el otro empieza con la cantidad de dígitos de una lista menos 1, ya que los index empiezan a contarse desde 0
    ayuda=int(0)
    elementos=int(len(lista1)-1)
#Los números espejo deben tener la misma cantidad de dígitos, así que se descartan si las listan tienen diferente longitud
    if len(lista1)!=len(lista2):
        print("Los números no son espejos")
#Ahora se determinan 2 variables que van a representar los dígitos
    else:
        a=lista1[0]
        b=lista2[elementos]
#Se compara el primer dígito del primer número con el último dígito del segundo número, si son diferentes se descartan...
        while ayuda<=len(lista1):
            if a!=b:
                print("Los números no son espejos")
                break
#...si son iguales, se compara el siguiente dígito del primer resultado con el dígito anterior del segundo número
            else:
                ayuda+=1
                elementos-=1
#Cuando la variable para sacar el index del primer número is igual o mayor que la variable del index del segundo número, significa que ya se revisaron todos los números, entonces significa que los números son espejos
        if ayuda>=elementos:
                    print("Los números son espejos")