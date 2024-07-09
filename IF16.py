def IF16 ():
    print("----------------------------")
    print("Tarifa del taxi")
    print("----------------------------")
    ki=float(input("ingrese el monto: "))

    if ki < 10:
        tarifa = ki * 2.50
    else:
        tarifa= 10 * 2.50 + ( ki -10) *2.00
        print (f"La tarifa total del taxi es",tarifa )
