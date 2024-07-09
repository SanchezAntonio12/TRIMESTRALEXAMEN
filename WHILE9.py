def WHILE9 ():
    print("----------------------------")
    print("Suma  dígitos de un número")
    print("----------------------------")
    numero=int(input("Ingrese el numero:"))

    su=0
    while numero > 0:
        
        su=su + (numero %10)
        numero= numero // 10
        
        print(f"La suma de los digitos es {su}")
    
