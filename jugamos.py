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
            print (pistas(intento, p_secreta))
        else : 
            print ("Oh no, ha fallado intentelo de nuevo")
            print (pistas(intento, p_secreta))

def pistas(intento, p_secreta):

    pista = ""

    for i in range(len(intento)):
        if i < len(p_secreta):
            if intento[i] == p_secreta[i]:
                pista += "[" + intento[i] + "]" #Esto seria que la posicion es cocrrecta
    
    print ("Pista: " + pista)


    
if __name__ == "__main__":
    juego()