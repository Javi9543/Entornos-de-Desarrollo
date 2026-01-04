verbo = str(input("Introduce un verbo: "))
vocales = ('aeiouAEIOU')
verbo_final = ""

if verbo.endswith("ie"):
    car= ""
    contador = 0
    for i in verbo:
        if contador < len(verbo) -2:
            car = car + i
        contador = contador + 1
    verbo_final = car + "ing"

elif verbo.endswith("e"):
    if verbo == "be" or verbo.endswith("ee"):
        verbo_final = verbo + "ing"
    else:
        car= ""
        contador = 0
        for i in verbo:
            if contador < len(verbo) -1:
                car = car + i
            contador = contador + 1
        verbo_final = car + "ing"
else:
    verbo_final = verbo + "ing"

print ("Su verbo conjugado es: ", verbo_final)