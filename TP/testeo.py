
import math
import random
def productos():
    with open("productos.txt") as file_object:
        productos = file_object.read()
        return productos

cadena = productos()
def lectura(cadena):
    contador = 0
    lista = []
    Char = ""
    newChar = ""
    nuevaLista = []
    for i in cadena:
        if i == "\n":
            Char += ","
        else:
            Char += i
    for i in Char:
        if i != ",":
            newChar += i
        else:
            nuevaLista.append(newChar)
            newChar = ""
            contador += 1
            if contador % 3 == 0 and contador != 1:
                lista.append(nuevaLista)
                nuevaLista = []
    return lista

print(lectura(cadena))

def buscar_producto(lista_productos):
    i = random.randrange(0,len(lista_productos)+1)
    return lista_productos[i]
