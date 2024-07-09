def FOR4 ():
    print("----------------------------")
    print("imprimir numeros impares")
    print("----------------------------")
    n = int(input("ingresa un numero entero: "))
    for i in range (1, n + 1, 2):
        impares = n - i
        print("los numeros impares son",impares)
