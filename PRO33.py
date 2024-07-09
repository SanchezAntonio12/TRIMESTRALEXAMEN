def PRO33 ():
    print("----------------------------")
    print("calcular imc")
    print("----------------------------")
    am = float(input("altura en metros: "))
    pkg = float(input("peso en kilogramos: "))

    # proceso
    imc = pkg / (am ** 2)

    # imprimir
    print(f"Tu IMC es {imc:.2f}")
