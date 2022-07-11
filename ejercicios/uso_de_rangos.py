#Sintaxis de range() = (inicio<opcional>, fin<requerido>, incremento<>opcional)

# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimelos

# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista:
    if numero % 3 == 0:
        print(numero)


lista2 = range(2, 7)

for numero in lista2:
    print(numero)

lista3 = range(3,11, 2)

for numero in lista3:
    print(numero)

