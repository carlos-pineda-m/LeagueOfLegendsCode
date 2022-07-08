# while funciona con elementos booleanos
# condicion = True
#
# while condicion:
#     print('Ejecutando ciclo while')
# else:
#     print('Fin del Ciclo while')

contador = 0

while contador <= 5:
    print(contador)
    contador += 1 #contador = contador + 1
else:
    print('Fin ciclo while')


contador = 5

while contador >= 1:
    print(contador)
    contador -= 1
else:
    print('Fin ciclo while')


""" Uso del for y break

cadena = "Hola"

for letra in cadena:
    print(letra)
else:
    print('fin ciclo for')



for letra in 'Holanda':
    if letra == "a":
        print(f'Letra encontrada: {letra}')
        break
else:
    print('fin ciclo for')

#con el comando break rompe un ciclo

"""

# for i in range(6):
#     if i % 2 == 0:
#         print(f'Valor: {i}')
#
# for i in range(6):
#     if i % 2 != 0:
#         continue
#     print(f'Valor: {i}')