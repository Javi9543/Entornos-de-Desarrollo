try:
    n_alumn = int(input("Introduzca el numero de alumnos"))
    c_tot = 0 
except:
    print("Introduzca solo numeros, o numeros enteros")


if n_alumn >= 100:
    c_tot = n_alumn * 65
    print (f"El total a pagar es de {c_tot}")

elif n_alumn >= 50 and n_alumn <= 99:
    c_tot = n_alumn * 70 
    print (f"El total por alumno es de {c_tot}")

elif n_alumn >= 30 and n_alumn <= 49:
    c_tot = n_alumn * 95
    print (f"El total por alumno es de {c_tot}")

elif n_alumn <= 30:
    c_tot = 4000 / n_alumn
    print (f"El total por alumno es de {c_tot}")
