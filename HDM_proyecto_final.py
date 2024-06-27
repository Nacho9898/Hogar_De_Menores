import Datos_del_personal_con_def as ls

x = 0
op = 0
op1 = 0
op2 = 0
op3 = 0
op4 = 0



# Menú
while x == 0 :
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
        ls.lista_del_personal1()
            

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