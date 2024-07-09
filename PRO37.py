def PRO37 ():
    print("----------------------------")
    print("Promedio de 5 examenes")
    print("----------------------------")
    C1 = float(input("Ingrese primera calificasion: "))
    C2 = float(input("Ingrese segunda calificasion: "))
    C3 = float(input("Ingrese tercera calificasion: "))
    C4 = float(input("Ingrese cuarta calificasion: "))
    C5 = float(input("Ingrese quinta calificasion: "))
    #proceso
    promedio = (C1 + C2 + C3 + C4 + C5) / 5
    #imprimir
    print(f"El promedio final es {promedio:.2f}")
