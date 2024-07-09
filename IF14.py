def IF14 ():
    print("----------------------------")
    print("Palabra con mas de 5 letras")
    print("----------------------------")
    palabra = len(input("Ingresa una palabra: "))
    if palabra > 5:
        print("El texto tiene más de 5 letras")
    else:
        print("El texto no tiene 5 letras")
