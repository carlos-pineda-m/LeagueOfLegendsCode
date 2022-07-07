numero = int(input("Ingresa uno de los siguientes numeros 1 2 3: "))

if numero == 1:
    numeroTexto = 'Numero uno'
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else:
    print('Valor fuera de rango')

print(f'Numero propocionado: {numero} - {numeroTexto}')

#print("Condicion Verdadera") if condicion else print("Condicion Falsa")
#Se puede ocupar if y else en un codigo simplificado corto en una sola linea