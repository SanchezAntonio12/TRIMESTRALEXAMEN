def PRO43 ():
    print("----------------------------")
    print("calcular la base del cilindro")
    print("----------------------------")
    radio = float(input("ingresa el radio: "))
    altura = float(input("ingrese la altura: "))
    pi = float(input("ingrese el valor de pi: "))
    #proceso
    areab = pi * radio
    areal = pi * radio * altura
    volumen = areab * altura
    #imprimir
    print("el area de base es",areab)
    print("el area lateral es",areal)
    print("el volumen es",volumen)
