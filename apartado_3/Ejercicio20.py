try:
    
    peso = int(input("Introduzca el peso del paquete: "))
    destino = input(("Introduzca la zona de destino del paquete: "))
    cost_tot = 0

    if destino == "America del Norte" or destino == "america del norte":
        cost_tot = peso + 24.00

    elif destino == "America del sur" or destino == "america del sur":
        cost_tot = peso + 21.00

    elif destino == "America_Central" or destino == "america central":
        cost_tot = peso + 20.00

    elif destino == "Europa" or destino == "europa":
        cost_tot = peso + 10.00

    elif destino == "Asia" or destino == "asia":
        cost_tot = peso  + 18.00

    print (f"El costo total de su envio es de {cost_tot}")
    
except ValueError:
    print("introduzca numeros enteros")