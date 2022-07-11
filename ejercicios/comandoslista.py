

nombres = ["Juan", "Karla", "Ricardo", "Maria"]

print(type(nombres))

# acceder a los elementos de una lista [] = Acceso a los indices de la lista

print(nombres[3])
print(nombres[2])

# acceder a los elementos de manera inversa

print(nombres[-1])
print(nombres[-2])

#imprimir un rango

print(nombres[0:2]) #Sin incluir el indice 2

#ir del inicio de la lista al indice 3 (sin incluirlo)

print(nombres[:3])

#Desde el indice indicado hasta el final

print(nombres[1:])

#Cambiar un valor de la lista

nombres[3] = "Ivone"

print(nombres)

#iterar una lista

for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista")

#preguntar el largo de una lista

print(len(nombres))

#agregar un elemento a la lista

nombres.append("Lorenzo")

print(nombres)

#agregar un elemento en un indice

nombres.insert(1, "Octavio")

print(nombres)

#remover un elemento

nombres.remove("Octavio")
print(nombres)

#remover el ultimo valor agregado
nombres.pop()
print(nombres)

#eliminar un indice
del nombres[0]
print(nombres)

#limpiar la lista
nombres.clear()
print(nombres)

#borrar la lista por completo
del nombres
print(nombres)