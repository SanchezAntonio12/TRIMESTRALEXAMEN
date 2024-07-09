def FOR5 ():
    print("----------------------------")
    print("la suma de los numeros naturales")
    print("----------------------------")
    n = int(input("ingrese un numero entero: "))
    suma = 0
    for i in range (0, n + 1):
        suma += i
        print("La sume de los numero es",suma)
