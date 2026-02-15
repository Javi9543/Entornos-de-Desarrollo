texto = input('Introduzca el texto que quiera traducir al lenguaje ladron: ')
vocales = 'aeiou'
resultado = ""

for i in texto:
    vocal = False
    for j in vocales:
        if i == j:
            vocal = True
            break
    if vocal or i == " ":
        resultado = resultado + i
    else:
        resultado = i + 'o' + i

print (resultado)

