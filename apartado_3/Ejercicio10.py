import math
try:
    x1 = float(input("Introduzca el primer central"))
    y1 = float(input("Introduzca el segundo central"))
    x2 = float(input("Introduzca el tercer central"))
    y2 = float(input("Introduzca el cuarto central"))

    r1 = int(input("Introduzca el primer radio"))
    r2 = int(input("Introduzca el segundo radio"))
except ValueError:
    print("Ha introducido un valor erroneo, intentelo de nuevo")

sumrad = r1 + r2

difrad = abs(r1 - r2)

distrad = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distrad == 0:
    if r1 == r2:
        print("Las circunferencias son coincidentes")
    else:
        print("Las circunferencias son concentricas (una dentro de otra)")
elif distrad == sumrad:
    print ("Tangentes Exteriores")
elif distrad > sumrad:
    print ("Circunferencias Exteriores")
elif distrad == difrad:
    print("Tangentes Interiores")
elif distrad > difrad:
    print ("Las circunferencias son interiores, una dentro de otra sin tocarse")
else:
    print ("Secantes, se cortan en 2 puntos")