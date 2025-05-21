presupuestos = []
numero_presupuesto = 1
presupuesto_cancelado=False
from datetime import date

while True:

    print('-' * 20)
    print('Presupuesto N°', numero_presupuesto)
    print('-' * 20)
    cliente = input('Ingrese nombre de cliente o S para salir: ').upper()
    if not cliente:
        print("...............................")
        print("error, ingrese un cliente!!!! ")
        print("................................")
        continue
    if cliente == "S":
        break

    while True:
        try:
            dia = int(input('Ingrese día: '))
        except:
            print('Día inválido')
            continue
        
        try:
            mes = int(input('Ingrese mes: '))
        except:
            print('Mes inválido')
            continue

        try:
            anio = int(input('Ingrese año: '))
        except:
            print('Año inválido')
            continue
    
        try:
            fecha = date(anio, mes, dia)
            break
        except ValueError:
            print('Fecha inválida')
            continue
    
    while True:
     detalle = input ("Ingrese el detalle del presupuesto: ")
     if not detalle:
        print("-------------------------------------")
        print("Error, no se ingreso ningun detalle")
        print("Ingreso obligatorio!!!")
        print("-------------------------------------")
        continue
     
     cantidad = input("Ingrese cantidad del producto: ")
     if not cantidad:
         presupuesto_cancelado = True
         break
       
     try:
        cantidad = float(cantidad)
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            continue
     except ValueError:
        print("Ingrese un número válido para la cantidad.")
        continue

     precio_unitario = input("Ingrese precio por unidad:$ ")
     if not precio_unitario:
         presupuesto_cancelado = True
         break
     try:
        precio_unitario = float(precio_unitario)
        if precio_unitario <= 0:
            print("El precio debe ser mayor que cero.")
            continue
     except ValueError:
        print("El valor ingresado no es valido!!!!")
        continue
   
     presupuesto_cancelado = False
     break
    if cantidad and precio_unitario:
     precio_total= cantidad*precio_unitario
    else:
        print("Error no se puede guardar un presupuesto sin items!!!!")
        continue
    
    if not presupuesto_cancelado:
     presupuesto = numero_presupuesto, fecha, cliente, detalle, cantidad, precio_unitario, precio_total
     numero_presupuesto += 1
     presupuestos.append(presupuesto)

print('=' * 40)
print('Presupuestos ingresados:')
print('=' * 40)
for presupuesto in presupuestos:
    print("////////////////////////////////")
    print("---",'Presupuesto N°', presupuesto[0],"---")
    print("///Datos///")
    print('Fecha:', presupuesto[1])
    print('Cliente:', presupuesto[2])
    print("Detalle: ", presupuesto[3])
    print("+++++++++++++++++++++++++++++++")
    print("///Items///")
    print("Cantidad pedida: ", presupuesto[4])
    print("Precio unitario:$", presupuesto[5])
    print("Precio total:$", presupuesto[6])
    print("+++++++++++++++++++++++++++++++")