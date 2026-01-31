#Primera forma: 

palabras1 = ['Hola', 'Daw', 'Mundo']
longitud = []

for i in palabras1:
    longitud.append(len(i))

print ("Resultado con bucle for:", longitud)

#Segunda forma

palabras2 = ['Adios', 'Entornos', 'Formula 1']

long_map = list(map(len, palabras2))

print ("resultado con map", long_map)

#Tercera Forma
palabras3 = ['Buenas', 'Informatica, PC']

long_comp_listas = [len(i) for i in palabras3]

print ('Resultado con Compresion de listas: ', long_comp_listas)

