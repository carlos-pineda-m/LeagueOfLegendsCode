
numero = int(input("Por favor ingrese un numero: "))

if numero % 2 == 0:
    print(f'El valor de {numero} es par')
else:
    print(f'El valor de {numero} es impar')

edad = int(input(f'Ingrese su edad: '))

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")