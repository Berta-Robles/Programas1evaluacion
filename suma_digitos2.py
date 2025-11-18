#Escriba un programa que pida un número y devuelva la suma de sus dígitos.
#Por ejemplo, si introduce el 243 devuelve 9.

def suma_digitos2():
    #pedir un número y lo leo como una cadena
    numero=input("Dime un número de varias cifras: ")
    suma=0
    permanecer=True#mientras permanecer sea verdadero el programa está en bucle.
    while(permanecer==True):
        suma=suma+(numero%10)#suma acumula los restos
        numero=numero/10
        print("suma= "+str(suma)+" numero= "+str(numero))
        if(numero<10):
            suma=suma+numero
            permanecer=False
    print(suma)

suma_digitos2()
