''' Mi codigo

edad = int(input("Proporciona tu edad (0-30): "))

infancia = 0 <= edad < 10
cambios = 10 <= edad < 20
trabajo = 20 <= edad <= 30

if infancia:
    print("La infancia es increible")
elif cambios:
    print("Muchos cambios y mucho estudio")
elif trabajo:
    print("Amor y comienza el trabajo")
else:
    print("Etapa de vida no reconocida")


'''
#El del profesor

edad = int(input('Proporciona tu edad: '))
mensaje = None

if 0 <= edad < 10:
    mensaje = 'La infancia es increíble...'
elif  10 <= edad < 20:
    mensaje = 'Muchos cambios, mucho estudio...'
elif  20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    mensaje = 'Etapa de vida NO reconocida'

print(f'Tu edad es: {edad}, {mensaje}')