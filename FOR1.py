def FOR1 ():
    print("----------------------------")
    print("Tabla de Multiplicar")
    print("----------------------------")
    n = int(input("ingrese un numero: "))    
    for i in range (1,12 + 1):
        resultado = n * i
        print(n, "x",i,"=", resultado)
       
