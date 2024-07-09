def PRO35 ():
    print("----------------------------")
    print("metros a pies y pulgadas")
    print("----------------------------")
    metros = float(input("Ingresa la cantidad de metros: "))
    #proceso
    pies = metros / 0.3048
    pulgadas = metros / 0.0254
    #imprimir
    print(f"{metros} metros son {pies:.2f} pies y {pulgadas:.2f} pulgadas")
