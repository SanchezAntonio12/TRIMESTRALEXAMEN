def IF20 ():
    print("----------------------------")
    print("Años de experencia")
    print("----------------------------")
    año = float(input("Ingresa los años de experiencia: "))
    if año < 2:
        print("La categoría del trabajador es Junior")
    elif 2 <= año <5:
        print("La categoría del trabajador es Semi-Serio")
    else:
        print("La categoría del trabajador es Serio")

