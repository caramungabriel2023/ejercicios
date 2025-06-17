poblacion= open("/home/gabriel/Escritorio/logica/poblacion_identificada_provincia_agosto_2024.csv", "r") # r modo de apertira del archivo lectura
poblacion.readline() #leo la linea 1 para ignorarla.
lista_poblacion = poblacion.readlines() #leo el resto del archivo.
poblacion.close() # cierro el archivo porque ya lo tengo cargado en lista_poblacion.

#Inicializo variables
total_de_habitantes = 0
provincias = set()
generos = set()
rangos_edad = set()
nacionalidades = set()
paises_de_nacimiento = set()
explicacion_generos = {"F":"Femenino", "M":"Masculino", "X":"No binario"}

#Recorro la lista de poblacion
for linea in lista_poblacion: 
    datos = linea.split (",")
    cantidad_habitantes = int(datos[6])
    provincias.add(datos[1].strip())
    generos.add(datos[2].strip())
    rangos_edad.add(datos[3].strip())
    nacionalidades.add(datos[4].strip())
    paises_de_nacimiento.add(datos[5].strip())
    total_de_habitantes += cantidad_habitantes

#Ordenamiento de datos
generos = sorted(generos)
rangos_edad = sorted(rangos_edad)
nacionalidades = sorted(nacionalidades)
paises_de_nacimiento = sorted(paises_de_nacimiento)
provincias = sorted(provincias)

#Mostrar listados
print (f"++++++Listas presentes dentro del archivo+++++++")
print (f"----------Provincias Argentinas:------------")
cantidad = 0
for p in provincias:
    print ("#", p +".")
    cantidad += 1
print (f"Total de provincias: {cantidad}")
print ("-------Generos utilizados dentro del archivo:---------")
cantidad = 0
for g in generos:
    print("*", g +".")
    cantidad += 1
print(f"Total de generos: {cantidad}")
print("----------Edades quinquenales dentro del archivo-------")
cantidad = 0
for r in rangos_edad:
    print("+", r + ".")
    cantidad += 1
print(f"Total de rangos de edad: {cantidad}")
print ("----Nacionalidades presentes en el archivo------")
cantidad = 0
for n in nacionalidades:
    print("-", n + ".")
    cantidad += 1
print(f"Total de nacionalidades: {cantidad}")
print("----Paises de nacimiento presentes en el archivo------")
cantidad = 0
for p in paises_de_nacimiento:
    print("=", p + ".")
    cantidad += 1
print(f"Total de paises de nacimiento: {cantidad}")
print ("-----------------------------------------------")
print(f"Total de habitantes: {total_de_habitantes:,}") #imprime el total de habitantes :, separa el numero en millares osea con puntos.
print ("-------------FIN DEL PROGRAMA------------------")
