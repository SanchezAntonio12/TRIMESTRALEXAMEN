def PRO36 ():
    print("----------------------------")
    print("regla de 3")
    print("----------------------------")
    VA = float(input("ingrese primer valor: "))
    VB = float(input("ingrese segundo valor: "))
    VC = float(input("ingrese tercervalor: "))
    #proceso
    resultado = (VC * VB) / VA or (VA * VB) / VC
    #imprimir
    print(f"El cuarto valor proporcional es {resultado:.2f}")
