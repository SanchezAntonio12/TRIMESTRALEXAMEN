def PRO32 ():
    print("----------------------------")
    print("Grados celsius a fahrenheit y kelvin")
    print("----------------------------")
    celsius = float(input("ingrese grados celsius:"))
    #proceso
    F = (celsius*(9/5))+32
    K = celsius + 273,15
    #imprimir
    print(f"Grados celsius en fahrenheit es",F)
    print(f"Grados celsius en kelvin es",K) 
