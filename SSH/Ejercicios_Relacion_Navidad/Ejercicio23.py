cadena = str(input("Introduzca una cadena para corregirla: "))
car = ""
cad_final = ""

for i in cadena:
    es_car = ('a' <= i <= 'z') or ('A' <= i <= 'Z')

    if car == "." or car == "," and es_car:
        cad_final = cad_final + " "
    
    if i != " " or car != " ":
        cad_final = cad_final + i
        car = i

print ("Cadena corregida: ", cad_final)