for i in range (1,31, 3):
    print(i)

cadena = input("ingrese algo: ").upper()
for letra in cadena:
    print(letra)

estructura = [(20, 40,10), ("river","boca"), (True,False)]
for iterador in estructura:
    print("1er FOR", iterador)
    for elemento in iterador:
        print("2do FOR", elemento)