verbo = (input("Introduzca un verbo (en ingles): "))
verbo_final = ""

if verbo.endswith(('o', "ch", "s", "sh", "x", "z")):
    verbo_final = verbo + "es"
elif verbo.endswith("y"):
    car: str = ""
    contador = 0
    for i in verbo:
        if contador < len(verbo) -1:
            car = car + i
        contador = contador + 1
    verbo_final = car + "ies"
else:
    verbo_final = verbo + "s"

print (verbo_final)