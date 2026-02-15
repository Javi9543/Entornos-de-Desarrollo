try:
    dado = int(input("Introduzca la cara obtenida del dado para saber su cara opuesta"))
    
    num_a_cad = ""

    if dado == 1:
        num_a_cad = "Seis"
        print (f"La cara  opuesta de {dado} es {num_a_cad}")

    elif dado == 2:
        num_a_cad = "Cinco"
        print (f"La cara  opuesta de {dado} es {num_a_cad}")

    elif dado == 3: 
        num_a_cad = "Cuatro"
        print (f"La cara  opuesta de {dado} es {num_a_cad}")

    elif dado == 4:
        num_a_cad = "tres"
        print (f"La cara  opuesta de {dado} es {num_a_cad}")

    elif dado == 5:
        num_a_cad = "Dos"
        print (f"La cara  opuesta de {dado} es {num_a_cad}")

    elif dado == 6:
        num_a_cad = "Uno"
        print (f"La cara  opuesta de {dado} es {num_a_cad}")

    elif dado < 1 or dado >6:
        print ("ERROR numero incorrecto")

except ValueError:
    print("Introduzca un numero entero no cadenas")