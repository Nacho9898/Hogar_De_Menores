
# Definiciones e imports
import lb_op_1 as lb1
import Login

x = 0
op = 0
op1 = 0
op2 = 0
op3 = 0
op4 = 0
acceso_login = 0

#############################################################

# Login
intentos = 0
while intentos < 3:
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese Contraseña: ")
    if Login.login(usuario, contraseña):
        print("Bienvenido")
        acceso_login = True
        # Menú
    while (x==0):
        print("""
=====================================
|                                   |
|        Bienvenido al menú         |
|         Hogar de menores          |
|                                   |
=====================================""")
        print("1) Datos de menores")
        print("2) Datos del personal")
        print("3) Observaciones de menores")
        print("4) Salir")
        op = int(input("Por favor elige una opción: "))
        print()
        # Opciones
        if op == 1:
            while op1 == 0:
                print("Usted eligio la opción 1")
                print("""
    A continuación por favor
    selecione una opción

    1) Ingresar datos del menor
    2) Consultar datos del menor
    """)
                op1 = int(input("Por favor elige una opción: "))
                if op1 == 1:
                    lb1.ingresar_datos()
                    print("""
    ¿Desea volver al menú de la opción 1?
    1) Si
    2) No
    """)
                    op2 = int(input("Por favor elige una opción: "))
                    if op2 == 1:
                        op1 = 0
                elif op1 == 2:
                    if datos_del_menor:
                        # Solicitar el RUT para buscar los datos
                        rut_consulta = input("Ingrese el RUT del menor que desea consultar: ")
                        if "Rut" in datos_del_menor and datos_del_menor["Rut"] == rut_consulta:
                            lb1.consultar_datos(datos_del_menor)  # Mostrar los datos si el RUT coincide
                        else:
                            print("El RUT ingresado no coincide con los datos ingresados anteriormente.")
                    else:
                        print("No se han ingresado datos de ningún menor.")
                    print("""
    ¿Desea volver al menu principal?
    1) Si
    2) Salir
    """)
            op2 = int(input("Por favor elige una opción: "))
            if op2 == 1:
                continue
            elif op2 == 2:
                break


        elif op == 2:
            print("Usted eligio la opcion 2")
            print("""
    A continuación por favor
    selecione una opción

    1) Ingresar datos del personal
    2) Consultar datos del personal
    """)
            

        elif op == 3:
            print("Usted eligio la opcion 3")
            print("""
    A continuación por favor
    selecione una opción

    1) Ingresar observaciones
    2) Consultar consultar observaciones
    """)
        elif op == 4:
            print("Usted eligio la opcion 4")
            break
    else:
        intentos += 1
        print("""Inicio de sesion incorrecto.

Recuerda que Usuario y Contraseña deben ser iguales.
te quedan""", 3 - intentos, "intentos")
    break
if intentos == 3:
    print()
    print("Se ha bloqueado su cuenta. Intentelo mas tarde")