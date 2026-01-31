lexico = {
    "merry": "god",
    "christmas" : "jul",
    "and" : "och",
    "happy" : "gott",
    "new" : "nytt",
    "year" : "ar"
}

frase = input("Introduce una frase en ingles: ")

lista_ingles = frase.lower().split() #convertir a texto la lista de palabras

frase_nueva = map(lexico.get, lista_ingles) #sirve para buscar la palabra y su traduccion en  el diccionario

frase_traducida = list(frase_nueva) #traducir frase al sueco

print ("Tu frase nueva es: ", frase_traducida)

