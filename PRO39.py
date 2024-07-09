def PRO39 ():
    print("----------------------------")
    print("Triangulo segun su area por base y altuta")
    print("----------------------------")
    base = float(input("Ingresa la longitud de la base: "))
    altura = float(input("Ingresa la longitud de la altura: "))
    #proceso
    areaT= (base * altura) / 2
    #imprimir
    print(f"El área del triángulo es {areaT:.2f}")
