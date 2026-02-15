import random

colores = ['rojo', 'azul', 'amarillo', 'verde', 'marron', 'morado','rosa', 'negro', 'fucsia']

color_original = random.choice(colores) #sirve para elegir un color aleatorio en este caso

print (color_original)

letras = list(color_original)
random.shuffle(letras)          #esto hace el anagrama mezclando las letras del color
anagrama = "".join(letras)

print ("color Anagrama: ", anagrama)

#Adivinar color

coloru = ""
while coloru != color_original:
    coloru = input ("Adivine el nombre del color: ")

    if coloru == color_original:
        print ("Correcto!")