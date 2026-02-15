import os
import time

alfabeto = {
    'a':'alfa',
    'b' : 'bravo',
    'c' : 'charlie',
    'd' : 'delta',
    'e' : 'echo',
    'f' : 'foxtrot',
    'g' : 'golf',
    'h' : 'hotel',
    'i' : 'india', 
    'j' : 'juliett',
    'k' : 'kilo',
    'l' : 'lima',
    'm' : 'mike',
    'n' : 'november',
    'o' : 'oscar',
    'p' : 'papa',
    'q' : 'quebec',
    'r' : 'romeo',
    's' : 'sierra',
    't' : 'tango',
    'u' : 'uniform',
    'v' : 'victor',
    'w' : 'whiskey',
    'x' : 'x-ray',
    'y' : 'yankee',
    'z' : 'zulu'
}

texto = input("Introduzca su texto en lenguaje ICAO: ")
p_letra = 0.6
p_palabra = 1

mensaje = texto.split()
for i in mensaje: 
    for j in i:
        j.lower() #omitir letras capitales
        if j in alfabeto:
            cod_av = alfabeto[j]
            print ("Mensaje: ", cod_av)
            os.system(f'espeak "{cod_av}"')
            time.sleep(p_letra)
time.sleep(p_letra)