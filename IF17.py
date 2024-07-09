def IF17 ():
    print("----------------------------")
    print("Su nombre es largo, mediano o corto")
    print("----------------------------")
    nombre = input("ingrese su nombre:  ")
    tmñ = len(nombre)
    if tmñ > 5:
        print("El nombre es largo")
    elif 5 < tmñ < 8: 
        print("El nombre es mediano")
    else:
        print("El nombre es corto")
