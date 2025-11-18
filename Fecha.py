#Haz un programa que reciba una fecha en formato:
#" 4 de enero de 2026" y devuelva 4/01/26
def devuelve_dia(fecha):
    dia=""#una cadena donde vamos a construir número a numero el día
    cont=0
    longitud=len(fecha)
    while(cont<longitud):#mientras que contamos hasta un número menor que la longitud
        if(fecha[cont]!=" "):#detectamos si el carácter es un espacio o no
            dia=dia+fecha[cont]
            cont=cont+1#para que pueda avanzar a la siguiente letra/espacio
        else:
            cont=longitud
    return(dia)

def devuelve_mes(fecha):
    mes=""
    cont=0
    n_espacios=0
    longitud=len(fecha)
    while(cont<longitud):
        if(fecha[cont]==" "):
            n_espacios=n_espacios+1
        else:
            if(n_espacios==2):
                mes=mes+fecha[cont]
        cont=cont+1
    
    return(mes)
    

def fecha():
    #Tiene que leer una fecha en el formato adecuado
    fecha=raw_input("Introduce la fecha en el formato: 4 de enero de 2026 ")
    dia=devuelve_dia(fecha)
    mes=devuelve_mes(fecha)
    #anio=devuelve_anio(fecha)
    print(dia)
    print(mes)
    
fecha()
    #Tengo que aislar el día, mes y año: 4,enero,2026
    #lo hago con tres funciones; devuelve_dia(fecha),devuelve_mes(fecha),devuelve_anio(fecha)
    #Transformo el mes en un numero: enero->01
    #Concateno el día+mes+año, separados por "/"
    
