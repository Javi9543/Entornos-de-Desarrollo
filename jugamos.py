import random
def juego():
    palabra = ["coche" , "volante" , "escape", "rueda"]
    intento = ""
    p_secreta = random.choice(palabra)

    while intento != p_secreta: 
        
        print(p_secreta) 
        intento = input("Introduzca una palabra relacionada con coches: ").lower()
        print(intento)

        if intento == p_secreta:
            print ("Enhorabuena has acertado la palabra correcta")
        else : 
            print ("Oh no, ha fallado intentelo de nuevo")   

juego()