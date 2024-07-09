def PRO34 ():
    print("----------------------------")
    print("Calcular horas trabajadas")
    print("----------------------------")
    ht = float(input("Ingrese las horas trabajadas: "))
    sh = float(input("Ingrese el salario por hora: "))
    he = float(input("Ingrese el número de horas extra: "))
    #proceso
    st = ht * sh
    se = he * sh * 2
    smt = st + se
    #imprimir
    print("El salario total mensual es", st)
    print("El monto adicional por horas extra es", se)
