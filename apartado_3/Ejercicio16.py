try:
    tiempo = int(input("Introduzca los minutos que ha durado su llamada (empezando de 5 min): "))
    dias = input("Introduzca el dia que ha realizado la llamada: ")
    horaLlamada = input("Introduzca si la llamada fue durante la mañana o la tarde: ")
except ValueError:
    print("hubo un error en el programa")

c_tot_tiempo = 0
c_tot = 0

if tiempo >= 5 and tiempo < 8:
    c_tot_tiempo = tiempo * 1

elif tiempo >= 8 and tiempo < 10:
    c_tot_tiempo = tiempo * 0.80

elif tiempo == 10:
    c_tot_tiempo = tiempo * 0.70

elif tiempo > 10:
    c_tot_tiempo = tiempo * 0.50


if dias == "domingo":
    c_tot = c_tot_tiempo / 0.03

elif dias != "domingo" and horaLlamada == "mañana":
    c_tot = c_tot_tiempo / 0.15

elif dias != "domingo" and horaLlamada == "tarde":
    c_tot = c_tot_tiempo / 0.10

print (f"Total a pagar es: {c_tot}")