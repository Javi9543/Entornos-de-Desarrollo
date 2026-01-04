try:
    b = int (input("Introduzca la base"))
    e = int (input("Introduzca el exponente"))
        
    if e < 0:
        p = b ** e
        print(f"el resultado es {p}")
    elif e == 0:
        print("EL resultado es 1")
    else:
        p = b**e / 1
    print(f"El resultado es {p}")

except ValueError:
    print("Introduzca numeros no cualquier otro valor")

