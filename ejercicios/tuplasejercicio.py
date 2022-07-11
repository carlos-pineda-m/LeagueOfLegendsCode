# Dada la siguiente tupla,
# crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)

# tuplalista = list(tupla)
#
# del tuplalista [0]
# del tuplalista [1]
# del tuplalista [3]
# del tuplalista [3]
# print(tuplalista)


# for i in tuplalista:
#     if i < 5:
#         print(i)

lista = []
for x in tupla:
    if x < 5:
        lista.append(x)

print(lista)