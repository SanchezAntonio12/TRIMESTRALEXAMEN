def PRO38 ():
    print("----------------------------")
    print("convertir doloares a euros")
    print("----------------------------")
    dolares = float(input("Ingresa el valor en dólares: "))
    #proceso
    euros = dolares * 0.84  
    #imprimir
    print(f"{dolares:.2f} dólares son {euros:.2f} euros")
