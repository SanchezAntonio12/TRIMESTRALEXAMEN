def FOR3 ():
    print("----------------------------")
    print("contar vocales en una cadena")
    print("----------------------------")
    cadena = input("ingresa un texto: ")
    contador = 0
    for letra in cadena: 
          contador += 1
          print("La cantidad de vocal es",contador)
