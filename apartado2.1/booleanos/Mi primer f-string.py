try:
    nombre = str(input("Introduce su nombre"))
    edad = int(input("Introduce tu edad"))

    print (f'Hola, {nombre}, tienes {edad}, años')

    decimal = 2.3456677

    print (f'decimal = {decimal:6.3f}')
    
except ValueError:
    print("Hubo un error en el programa, para el nombre solo escriba caracteres y para la edad solo escriba numeros enteros")