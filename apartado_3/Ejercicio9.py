try: 
    a = int(input("Introduzca el primer numero ENTERO"))
    b = int(input("Introduzca el segundo numero ENTERO"))
    c = int(input("Introduzca el segundo numero ENTERO"))
except ValueError:
    print("INTRODUZCA SOLO NUMEROS ENTEROS")

try:
    if a >= b and a >= c:
        if b >= c:
            print(f"{a}, {b}, {c}")
        else:
            print(f"{a}, {c}, {b}")
    elif b >= a and b >= c:
        if a >= c:
            print(f"{b}, {a}, {c}")
        else:
            print(f"{b}, {c}, {a}")
    else:
        if a >= b:
            print(f"{c}, {a}, {b}")
        else:
            print(f"{c}, {b}, {a}")
except:
    print("Hubo un problema, intentelo de nuevo")