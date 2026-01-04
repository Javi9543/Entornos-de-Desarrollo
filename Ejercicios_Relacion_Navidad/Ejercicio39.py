import random

n = random.randint(0,20)
numu = 0
intentos = 0

nombre = input ("Bienvenido a adivina el numero, introduzca su nombre: ")
print (f'Bueno {nombre}, estoy pensando un numero entre 1 y 20')

while numu != n:

    try:
        numu = int(input('Intente adivinarlo: '))
        intentos += 1


        if numu < n:
            print ("El numero introducido es muy bajo")

        elif numu > n:
            print ("El numero introducido es muy alto")

        elif numu == n:
            print (f'Buen trabajo {nombre}, has advinado el numero en {intentos} intentos.')
    except ValueError:
        print ("El dato introducido debe ser un NUMERO ENTERO")

