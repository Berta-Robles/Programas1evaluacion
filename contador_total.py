def menu():
    #menu
    print("elige una opción (1-6): ")
    print("1. Contar el numero de letras")
    print("2. Número de consonantes")
    print("3. Número de vocales")
    print("4. Número de palabras")
    print("5. Número de veces que aparece la letra o")
    print("6. Encripta el mensaje sustituyendo cada letra por la siguiente en el abecedario")

def contar_letras(texto):
    print("Tiene "+str(len(texto))+" caracteres")
    
def contar_consonantes(texto):
    vocales="aeiouAEIOU"
    numero="1234567890"
    n_consonantes=0
    for letra in texto:
        if(not((letra in vocales) or (letra==" ") or (numero))):
            n_consonantes=n_consonantes+1
    print("Tiene "+str(n_consonantes)+" consonantes")

def contar_vocales(texto):
    vocales="aeiouAEIOU"
    numero="1234567890"
    n_vocales=0
    for letra in texto:
           if(letra in vocales):
               n_vocales=n_vocales+1
    print("Tiene "+str(n_vocales)+" vocales")
    
def contar_palabras(texto):
    n_palabras=0
    for letra in texto:
        if(letra==" "):
            n_palabras=n_palabras+1
    print("Tiene "+str(n_palabras+1)+" palabras")

def contar_oes(texto):
    n_oes=0
    for letra in texto:
        if(letra=="o" or letra=="O"):
            n_oes=n_oes+1
    print("Tiene "+str(n_oes)+" oes")

def encriptar(texto):
    texto_encriptado=""
    for letra in texto:
        texto_encriptado=texto_encriptado+chr(ord(letra)+1)
    print("TEXTO ENCRIPTADO: "+texto_encriptado)

def contador_total():
    texto=raw_input("Introduce una frase: ")
    menu()
    opcion=input("Elige una opción del 1 al 6: ")
    if(opcion==1):
        contar_letras(texto)
    if(opcion==2):
        contar_consonantes(texto)
    if(opcion==3):
        contar_vocales(texto)
    if(opcion==4):
        contar_palabras(texto)
    if(opcion==5):
        contar_oes(texto)
    if(opcion==6):
        encriptar(texto)

contador_total()
