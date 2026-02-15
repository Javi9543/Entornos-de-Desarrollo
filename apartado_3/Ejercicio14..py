try:
    PrecioProducto = int(input("Introduzca el precio inicial del producto"))
    tipoProdcto = input("Introduzca el tipo de producto (A o B)")
    tamañosProducto = int(input("Introduzca el tamaño de producto (1 o 2)"))

    PrecioFinalProducto = 0

    if tipoProdcto == "A" and tamañosProducto == 1:
        PrecioFinalProducto = PrecioProducto * 0.20
        print (f"Recibirá {PrecioFinalProducto} euros")
    elif tipoProdcto == "A" and tamañosProducto == 2:
        PrecioFinalProducto = PrecioProducto * 0.30
        print (f"Recibirá {PrecioFinalProducto} euros")

    elif tipoProdcto == "B" and tamañosProducto == 1:
        PrecioFinalProducto = PrecioProducto / 0.30
        print (f"Recibirá {PrecioFinalProducto} euros")

    elif tipoProdcto == "B" and tamañosProducto == 2:
        PrecioFinalProducto = PrecioProducto / 0.50
        print (f"Recibirá {PrecioFinalProducto} euros")
except ValueError:
    print("Introduzca numeros enteros")