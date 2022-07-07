"""Codigo propio
mes = int(input("Proporcione el numero de su mes favorito (1 al 12): "))

primavera = mes <= 3
verano = 3 < mes <= 6
otono = 6 < mes <= 9
invierno = 9 < mes <= 12

if primavera:
    primavera = "Primavera"
    print(f'Su mes de numero {mes} pertenece a la estacion de: {primavera}')
elif verano:
    verano = "Verano"
    print(f'Su mes de numero {mes} pertenece a la estacion de: {verano}')
elif otono:
    otono = "Otoño"
    print(f'Su mes de numero {mes} pertenece a la estacion de: {otono}')
else:
    invierno = "Invierno"
    print(f'Su mes de numero {mes} pertenece a la estacion de: {invierno}')

"""

#Codigo del profesor
mes = int(input("Proporcione el numero de su mes favorito (1 al 12): "))

estacion = None

if mes == 1 or mes == 2 or mes == 3:
    estacion = "Invierno"

if mes == 4 or mes == 5 or mes == 6:
    estacion = "Primavera"

if mes == 7 or mes == 8 or mes == 9:
    estacion = "Verano"

if mes == 10 or mes == 11 or mes == 12:
    estacion = "Otoño"
else:
    print('Su estacion elegida es no valida')

if estacion == "Invierno":
        print(f'Su mes de numero {mes} pertenece a la estacion de: {estacion}')
elif estacion == "Primavera":
    print(f'Su mes de numero {mes} pertenece a la estacion de: {estacion}')
elif estacion == "Verano":
    print(f'Su mes de numero {mes} pertenece a la estacion de: {estacion}')
elif estacion == "Otoño":
    print(f'Su mes de numero {mes} pertenece a la estacion de: {estacion}')
