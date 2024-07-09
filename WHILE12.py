def WHILE12 ():
    print("----------------------------")
    print("contador de digitos")
    print("----------------------------")
    numero=int(input("ingrese numero:"))
    x=0
    c=numero
    while numero > 0:
        numero=numero//10
        x=x+1
        print(f"El numero {c} tiene un {x} dígitos")
    
