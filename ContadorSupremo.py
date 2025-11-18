def ContadorSupremo():
    frase=raw_input("Dime una frase: ")#Leemos una cadena
    print("El texto tiene "+str(len(frase))+" caracteres")#Contamos el número de letras
    letra=""
    vocales="aeiouAEIOU"
    cont=0
    cont2=0
    cont3=0
    os=frase.lower().count("o")
    abcdario="abcdefghijklmnñopqrstuvwxyz"
    cambioabc="bcdefghijklmnñopqrstuvwxyza"
    palabras=frase.split()
    cantidad=len(palabras)
    for letra in frase:
        cont=cont+1
        print("letra= "+letra+" "+str(cont))
        if letra not in vocales:
            cont2=cont2+1
        else:
            cont3=cont3+1
    
    print("Hay en total "+str(cont2)+" consonantes")
    print("Y hay en total "+str(cont3)+" vocales")     
    print("Tiene una cantidad de "+str(cantidad)+" palabras")
    print("Dentro de esta frase hay "+str(os)+" letras o")

ContadorSupremo()
