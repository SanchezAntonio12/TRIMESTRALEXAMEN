def PRO30 ():
    print("----------------------------")
    print("Calcular el area de un trapecio")
    print("----------------------------")
    bm = float(input("base menor: "))
    bmr = float(input("base mayor: "))
    altura = float(input("Altura : "))

    # Calcular el área
    area = bm +  bmr * altura / 2
    #imprimir
    print("El área del trapecio es", area)
