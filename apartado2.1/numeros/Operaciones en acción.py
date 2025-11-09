
try:
    n1 = int(input('Introduzca un numero: '))
    n2 = int(input('Introduzca el segundo numero: '))
except:
    print ('Hubo un error al introducir uno de los dos numeros, recuerde que deben ser enteros')
    
suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2
div_ent = n1 // n2
resto_num = n1 % n2
pot = n1 ** n2

print(suma)
print(resta)
print(mult)
print(div)
print(div_ent)
print(resto_num)
print(resto_num)
print(pot)
