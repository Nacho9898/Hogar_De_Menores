import libreria as lb
lb.iniciar_sesion()
x=0



while x != 3:
    x=int(input("""
    ======= Menú Principal =======
    1) Ingresar datos del menor 
    2) Consultar datos del menor
    3) Salir                    """))
    if x == 1:
        lb.ingresar_datos()
    elif x == 2:
        lb.consultar_datos()
    elif x == 3:
        lb.salir()
    