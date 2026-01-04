lexico = {
    "merry":"god",
    "christmas":"jul",
    "and":"och",
    "happy":"gott",
    "new": "nit",
    "year":"ar"
}

frase_ingles = ["merry", "christams", "and", "happy", "new", "year"]

traduccion =  []

for i in lexico:
    frase = lexico[i]
    traduccion = traduccion + [frase]

print("Frase en ingles: ", frase_ingles)
print("")
print("Frase en sueco: ", traduccion)