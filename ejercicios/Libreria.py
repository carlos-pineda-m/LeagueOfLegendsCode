
print("Proporciona los siguientes datos del libro:")

nombre = input("Proporciona el nombre del libro: ")

id = int(input("Proporciona el ID: "))

precio = float(input("Propociona el precio: "))

envio = input("Indica si el envio es gratuito (True/False): ")

#codigo para cambiar de STRING a BOOL
if envio == "True":
    envio = True

elif envio == "False":
    envio = False
else:
    print("Valor Incorrecto, Debe escribir (True/False)")

print(f'''
    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Envio Gratuito: {envio}
''')

#la funcion bool siempre dara "True" siempre y cuando haya una variable booliana
