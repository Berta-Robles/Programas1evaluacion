def Contrasena():
    nom=raw_input("Como te llamas: ")
    print("Hola "+nom)    
    ap1=raw_input("Cual el tu primer apellido? ")
    ap2=raw_input("Y el segundo? ")
    fech=raw_input("por ultimo, en que año naciste? ")
    print("Tu contraseña es: "+(nom[0:3])+(ap1[0:3])+(ap2[0:3])+(fech[2:4]))
Contrasena()
