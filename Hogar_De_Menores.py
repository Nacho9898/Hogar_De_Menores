# Definiciones
datos_menor = {}  # lista para almacenar datos del menor
observación = []  # lista para almacenar observaciones del menor
op_3 = ("1", "2", "3")  # opciones para el menu

# Ingresar anotaciones/Observaciones de menores
while True:
    print()
    print("usted ha elegido la opcion 3")
    print()
    print("1.- Ingresar observasiones del menor")
    print("2.- Consultar observaciones del menor")
    print("3.- Regresar al menu principal")
    print()
    opcion = input("por favor elige una opción: ")

    if opcion == "3":
        print()
        print("usted ha elegido la opcion 3")
        print("Sera enviado al menu principal")
        break

    elif opcion == "2":
        print()
        print("usted ha elegido la opción 2")
        print("Por favor ingrese los siguientes datos:")
        rut_menor = input("Ingrese el RUT del menor: ") 

        if rut_menor in datos_menor.keys():
            print("Observaciones del menor: ")
            for validar in datos_menor[rut_menor]:
                print(validar)

    elif opcion == "1":
        print()
        print("usted ha elegido la opción 1")
        print("por favor ingrese los siguientes datos del menor:")

        # obtener datos del menor
        datos_menor["nombres"] = input("Nombres: ")
        datos_menor["apellidos"] = input("Apellidos: ")
        datos_menor["fecha_nacimiento"] = input("Fecha de nacimiento: ")
        datos_menor["nacionalidad"] = input("Nacionalidad: ")
        datos_menor["rut"] = input("RUT: ")
        datos_menor["sala"] = input("Sala: ")
        datos_menor["observaciones"] = input("Observaciones: ")