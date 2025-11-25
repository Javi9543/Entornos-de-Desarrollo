nota = int(input("Introduzca su nota"))
edad = int(input("Introduzca su edad"))
sexo = input("Introduzca su sexo (M o F)").upper()

if nota >= 5 and edad >= 18 and sexo == "F":
    print("Aceptada")
elif nota >= 5 and edad >= 18 and sexo == "M":
    print("Posible")
else:
    print("No Aceptada")