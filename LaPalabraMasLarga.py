def LaPalabraMasLarga():
    pala1("Dime una palabra cualquiera: ")
    longitud=len(pala1)
    pala2("Dime otra palabra cualquiera: ")
    longitud2=len(pala2)
    print("La palabra "+pala1+" tiene "+str(longitud1)+" letras") 
    for cont in range(0,longitud1):
        print(palabra[cont])
    print("Y la palabra "+pala2+" tiene "+str(longitud2)+" letras")
    for cont in range(0,longitud2):
        print(palabra[cont])
    palabras=[pala1,pala2]
    maximo=max(palabras)
    print("la palabra más larga es "+maximo)

LaPalabraMasLarga()
