def PRO29 ():
    print("----------------------------")
    print("Calcular el perímetro del rectángulo")
    print("----------------------------")
    AB = float(input("Ingrese la longitud del lado AB: "))
    BC = float(input("Ingrese la longitud del lado BC: "))
    CD = float(input("Ingrese la longitud del lado CD: "))
    DA = float(input("Ingrese la longitud del lado DA: "))

    # proceso
    pr = AB +  BC + CD + DA
    #imprimir
    print(f"El perímetro del rectángulo es {pr}")
