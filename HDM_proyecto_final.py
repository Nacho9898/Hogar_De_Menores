import lb_op_1 as lb1
import Login
import lista_del_personal1 as ls

x = 0
op = 0
op1 = 0
op2 = 0
op3 = 0
op4 = 0
acceso_permitido = False

# Login
intentos = 0
while intentos < 3:
    print("""
Ingrese su usuario, recordar que 
tanto el usuario como la contraseña deben ser iguales. 

EJ: Josef1234""")
    print()
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese Contraseña: ")

    if Login.login(usuario, contraseña):
        print("Bienvenido")
        acceso_permitido = True
        break
    else:
        intentos += 1
        print(f"Inicio de sesión incorrecto. Te quedan {3 - intentos} intentos")
        
if intentos == 3:
    print("Se ha bloqueado su cuenta. Inténtelo más tarde")

# Menú
while x == 0 and acceso_permitido:
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
    
    if op == 1:
        while op1 == 0:
            print("Usted eligió la opción 1")
            print("""
    A continuación por favor
    seleccione una opción

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
                lb1.consultar_datos()
                print("""
    ¿Desea volver al menú principal?
    1) Si
    2) Salir
    """)
                op2 = int(input("Por favor elige una opción: "))
                if op2 == 1:
                    op1 = 0
                else:
                    x = 1

    elif op == 2:
        while op3 == 0:
            print("Usted eligió la opción 2")
            print("""
    A continuación por favor
    seleccione una opción

    1) Ingresar datos del personal
    2) Consultar datos del personal
    """)
            op3 = int(input("Por favor elige una opción: "))
            if op3 == 1:
                lb2.ingresar_datos()
                print("""
    ¿Desea volver al menú de la opción 2?
    1) Si
    2) No
    """)
                op4 = int(input("Por favor elige una opción: "))
                if op4 == 1:
                    op3 = 0
            elif op3 == 2:
                lb2.consultar_datos()
                print("""
    ¿Desea volver al menú principal?
    1) Si
    2) Salir
    """)
                op4 = int(input("Por favor elige una opción: "))
                if op4 == 1:
                    op3 = 0
                else:
                    x = 1

    elif op == 3:
        while op1 == 0:
            print("Usted eligió la opción 3")
            print("""
    A continuación por favor
    seleccione una opción

    1) Ingresar observaciones
    2) Consultar observaciones
    """)
            op1 = int(input("Por favor elige una opción: "))
            if op1 == 1:
                lb3.ingresar_observaciones()
                print("""
    ¿Desea volver al menú de la opción 3?
    1) Si
    2) No
    """)
                op2 = int(input("Por favor elige una opción: "))
                if op2 == 1:
                    op1 = 0
            elif op1 == 2:
                lb3.consultar_observaciones()
                print("""
    ¿Desea volver al menú principal?
    1) Si
    2) Salir
    """)
                op2 = int(input("Por favor elige una opción: "))
                if op2 == 1:
                    op1 = 0
                else:
                    x = 1

    elif op == 4:
        print("Usted eligió la opción 4")
        x = 1

print("Gracias por usar el programa. Adiós.")