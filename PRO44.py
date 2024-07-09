def PRO44 ():
    print("----------------------------")
    print("tres lados del triangulo usando semiperimetro y perimetro")
    print("----------------------------")
    LA = float(input("ingrese primer lado: "))
    LB = float(input("ingrese segundo lado: "))
    LC = float(input("Ingrese tercer lado: "))
    #proceso de semiperimetro
    sp = (LA + LB + LC) / 2
    #proceso de ley heron
    area = (sp * (LA) * (LB) * (LC)) ** 0.5
    #proceso de perimetro
    p = LA + LB + LC 
    #imprimir
    print("el area del triamgulo es",area)
    print("el perimetro del triangulo es",p)
    print("el semiperimetro del triangulo es",sp)
