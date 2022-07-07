#Operadores Logicos
valor = int(input('Proporcione un valor: '))

minimo = 0
maximo = 5

rango = valor >= minimo and valor <= maximo


if rango == True:
    print(f'El valor {valor} esta en el rango')
else:
    print(f'El valor {valor} no esta en el rango')

    
vacaciones = False
descanso = False

if vacaciones or descanso:
    print("Puedes asistir al juego")
else:
    print("No puedes asistir")


#Operaciones con and y or

edad = int(input("Proporciona tu edad: "))

veintes = edad>=20 and edad<30

print(veintes)

treintas = edad>=30 and edad<40

print(treintas)


#Caracter de escape \ para omitir fin de comandos en unas cremillas
if veintes or treintas:
    print(f'Tu edad: {edad} esta dentro del rango 20\'s y 30\'s')
    if veintes:
        print(f'Estas dentro de los 20\'s')
    elif treintas:
        print(f'Estas dentro de los 30\'s')
else:
    print(f'Tu edad: {edad} no esta dentro del rango de 20\'s y 30\'s')

#Generalmente todas las variables se ponen dentro de la funcion if
edad = int(input("Proporciona tu edad: "))

if (edad>=20 and edad<30) or (edad>=30 and edad<40):
    if (edad>=20 and edad<30):
        print(f'Estas dentro de los 20\'s')
    elif (edad>=30 and edad<40):
        print(f'Estas dentro de los 30\'s')
else:
    print(f'Tu edad: {edad} no esta dentro del rango de 20\'s y 30\'s')

#Simplificacion

if (20 <= edad < 30) or (30 <= edad < 40):
    if (20 <= edad < 30):
        print(f'Estas dentro de los 20\'s')
    elif (30 <= edad <40):
        print(f'Estas dentro de los 30\'s')
else:
    print(f'Tu edad: {edad} no esta dentro del rango de 20\'s y 30\'s')