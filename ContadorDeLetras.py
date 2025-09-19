def ContadorDeLetras():
    palabra=raw_input("Dime una palabra cualquiera: ")
    longitud=len(palabra)
    print("La palabra "+palabra+" tiene "+str(longitud)+" letras")
    for cont in range(0,longitud):#Cont es para la variable que le da range, que es el rango entre las cifras que le damos
        print(palabra[cont])
   

ContadorDeLetras()    
