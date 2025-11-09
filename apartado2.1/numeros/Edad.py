f_act = 2025

try:
    f_nacim = int(input('Introduzca su año de nacimiento: '))
    edad = f_act - f_nacim
    print ("Tienes: ",edad)
except:
    print ("Introduzca solo numeros")