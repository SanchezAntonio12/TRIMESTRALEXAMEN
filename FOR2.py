def FOR2 ():
    print("----------------------------")
    print("Numeros descendente")
    print("----------------------------")
    n = int(input("ingrese un numero: "))
    for i in range (11, 0, -1):
        descendente = i - n
        print("el numero es",descendente)
