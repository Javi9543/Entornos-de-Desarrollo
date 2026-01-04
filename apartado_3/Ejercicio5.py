try:
    usu = str(input("Crea un usuario"))
    cont = str(input("Crea una contraseña"))

    print("Usuario y Contraseña Registrados")

    usu1 = str(input("Introduzca su usuario"))
    cont1 = str(input("Introduzca su contraseña"))
except:
    print ("Ha habido un error, intentelo de nuevo")

try:
    if usu1 != usu or cont != cont1:
        print("Usuario o contraseña no coinciden, intentelo más tarde")
    else:
        print ("Usuario y contraseña validos, accediendo al sistema")
except:
