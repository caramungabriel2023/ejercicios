ejecuciones = 0
while True:
    
    valor =(input("ingrese un numero (con ENTER sale): "))
    if not valor:
        break
    
    valor = float (valor)
    ejecuciones = ejecuciones + 1
    
    if valor > 0:
        print(valor, "es positivo")
    elif valor < 0:
        print(valor, "es negativo")
    else:
        print(valor, "es cero")

if ejecuciones == 1:
    texto =  "ejecucion"
else:
    texto = "ejecuciones"

print("FIN DEL PROGRAMA", ejecuciones,texto)