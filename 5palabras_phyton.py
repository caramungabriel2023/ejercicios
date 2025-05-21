palabras = [] #lista vacia
print("---Ingrese palabras relacionadas con phyton---")
for vuelta in range(1, 6): # va a dar 5 vueltas sumando la funcion range
    leyenda = "ingrese " + str(vuelta) + "º palabra:" # leyenda es para que cuando me pida que ingrese valla poniendo primera palabra 2 palabra, etc.
    palabra = input(leyenda)
    palabras.append(palabra.lower()) # lower vuelve todo minuscula, se agrega a la lista vacia las palabras que ingresamos en el imput con append

palabras.sort() # sort() ordena.

print("*** Palabras ordenadas***")
for p in palabras:
    print(p)

print ("**********************")
