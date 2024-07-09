def WHILE10 ():
    print("----------------------------")
    print("Multiplo de un numero")
    print("----------------------------")
    n = int(input("Ingrese un número entero positivo: ")) 
    x = 1  
    c = 12  

    while x <= c:
        multiplo = n * x
        print(f"{n} x {x} = {multiplo}")
        x=x+1
