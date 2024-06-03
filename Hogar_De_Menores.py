
# definiciones

op_3 = 

# Ingresar anotaciones/Observaciones de menores

while True:
    print()
    print("usted ha elegido la opcion 3")
    print()
    print("1.- Ingresar observasiones del menor")
    print("2.- Consultar observaciones del menor")
    print("3.- Regresar al menu principal")
    print()
    input("por favor elige una opción: ")

    if op_3 == "1":
        print()
        print("""usted ha elegido la opcion 1
por favor ingrese los siguientes datos:
""")
        input("Nombres: ")
        input("Apellidos: ")
        input("Fecha de nacimiento: ")
        input("RUT: ")
        input("Sala: ")
        input("Observaciones: ")

    elif op_3 == "2":
        print()
        print("""usted ha elegido la opción 2
Por favor ingrese los siguientes datos:
""")
        input("Ingrese el RUT del menor: ")
        print()

    elif op_3 == "3":
        print()
        print("""usted ha elegido la opción 3
Sera enviado de regreso al menú principal
""")
        break