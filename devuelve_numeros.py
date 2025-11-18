#mostrar por pantalla los tres numeros anteriores
def muestra_anteriores(numero,correlativo):
    for cont in range(1,correlativo+1):
        print(numero+cont)

def muestra_posteriores(numero,correlativo):
    for cont in range(1,correlativo+1):
        print(numero-cont)
               
#mostrar por pantalla los tres numeros posteriores
def devuelve_numeros():
    numero=input("Dime un número: ")
    correlativo=input("Cuantos números anteriores y posteriores quieres: ")
    muestra_anteriores(numero,correlativo)
    muestra_posteriores(numero,correlativo)
    
devuelve_numeros()
