def PRO45 ():
    print("----------------------------")
    print("Calcule el impuesto de un producto")
    print("----------------------------")
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad de productos: "))
    #proceso
    impuesto = 0.10  
    subtotal = precio * cantidad
    it = subtotal * impuesto
    tp = subtotal + it
    #imprimir
    print(f"Subtotal es {subtotal:.2f}")
    print(f"Impuesto es (IVA) {it:.2f}")
    print(f"Total a pagar es {tp:.2f}")
