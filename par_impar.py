def par_impar():
    numero=input("Hasta que numero quieres clasificar pares o impares?: ")
    for cont in range (0,numero+1):
        if(cont%2==0):
            print(str(cont)+" PAR")
        else:
            print(str(cont)+" IMPAR")

par_impar()
