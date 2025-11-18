#Escriba un programa que pida un número y devuelva la suma de sus dígitos.
#Por ejemplo, si introduce el 243 devuelve 9.

def suma_digitos():
    #pedir un número y lo leo como una cadena
    numero=raw_input("Dime un número de varias cifras: ")
    longitud=len(numero)
    suma=0
    for cont in range(0,longitud):
        suma=suma+int(numero[cont])
    #trocearlo en cifras
    print(suma)
    #sumo o acumulo las cifras en una variable acumulativa
    ####
suma_digitos()
