f_act = 2025

while True:
    try: 
        f_nacim = int(input('Introduzca su año de nacimiento'))

        edad = f_act - f_nacim

        print (edad)
        break
    except:
        print("¡Vaya! ha introducido algo invalido intentelo de nuevo")