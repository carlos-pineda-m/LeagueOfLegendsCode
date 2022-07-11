#definir una tupla

frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)

#Saber el numero de elementos
print(len(frutas))

#iterar la lista
# for i in frutas:
#     print(i)

#Acceder a un elemento

print(frutas[0])

#acceder a un rango
print(frutas[0:1])#No incluye el primero
print(frutas[0:2])

#recorrer elementos

for fruta in frutas:
    print(fruta, end=' ') #para evitar el salto de linea

#cambiar valor de tupla convertir tupla x lista
# frutas[0] = 'Pera'

frutasLista = list(frutas)

frutasLista[0] = 'Pera'

frutas = tuple(frutasLista)

print('\n',frutas)

#eliminar la tupla
del frutas

print(frutas)