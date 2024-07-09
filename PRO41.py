def PRO41 ():
    print("----------------------------")
    print("Calcular el volumen de un cilindro")
    print("----------------------------")
    radio = float(input("Ingresa el radio del cilindro:  "))
    altura = float(input("Ingresa la altura del cilindro: "))
    #proceso
    volumenC = 3.14 * radio * altura
    #imprimir
    print(f"El volumen del cilindro es {volumenC:.2f} centímetros cúbicos")
