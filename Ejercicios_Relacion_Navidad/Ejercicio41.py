import random

palabras = ["tiger", "snake", "house", "apple", "cloud", "lemon"]

p_secreta = random.choice(palabras)
intento = ""

print ("Bienvenido al juego del lingo, Adivine la palabra")
print (" ")

while intento != p_secreta:
    intento = input("Introduce tu palabra: ").lower() #lo pongo en punto lower por si al usuario se el escapa alguna mayuscula
    pista = ""

    for i in range(len(intento)):
        if i < len(p_secreta):

            if intento[i] == p_secreta[i]:
                pista += '[' + intento[i] + ']'

            elif intento[i] in p_secreta:
                pista += '(' + intento[i] + ')'
            else:
                pista += intento[i]

        else: 
            pista = pista + intento

    print(f'Clue: {pista}')

print ("Palabra correcta! la palabra secreta es: ", p_secreta)