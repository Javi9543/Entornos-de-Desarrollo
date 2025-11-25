try:
    a = int(input("Introduzca el primer numero"))
    b = int(input("Introduzca el segundo numero"))
    c = int(input("Introduzca el tercer numero"))
except ValueError:
    print ("Asegurese de que son numeros enteros")

if (a == b and a == c):
    print ("Tu triangulo es equilatero")
elif (a == b) or (a == c) or (b == c):
    print ("Tu triangulo es isósceles")
elif (a**2 + b**2 == c**2) or (c**2 + b**2 == a**2) or (c**2 + b**2 == a**2):
    print ("Tu triangulo cumple pitagoras")
else:
    print("Tu triangulo es escaleno")