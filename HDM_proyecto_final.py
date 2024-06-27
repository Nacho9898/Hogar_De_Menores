import Libreria as lb

# Login
acceso_permitido = lb.login()

# Menú
if acceso_permitido:
    while True:
        print("""
=====================================
|                                   |
|        Bienvenido al menú         |
|         Hogar de menores          |
|                                   |
=====================================
1) Datos de menores
2) Datos del personal
3) Observaciones de menores
4) Salir
""")
        op = int(input("Por favor elige una opción: "))
        if op == 1:
            print("""Usted ha elegido la opción 1
Ahora que opción desea:

1) Ingresar Datos del menor
2) Consultar Datos del menor
3) Volver al menú principal
""")
            while True:
                op1 = int(input("Por favor elige una opción: "))
                if op1 == 1:
                    print("Usted ha elegido la opción 1")
                    lb.ingresar_datos()
                    break
                elif op1 == 2:
                    print("Usted ha elegido la opción 2")
                    lb.consultar_datos()
                    break
                elif op1 == 3:
                    print("Usted ha elegido la opción 3")
                    break
        elif op == 2:
            print("Usted ha elegido la opción 2")
            lb.lista_del_personal1()
        elif op == 3:
            print("""Usted ha elegido la opción 3
Ahora que opción desea:

1) Ingresar Observaciones
2) Consultar Observaciones
3) Volver al menú principal
""")
            while True:
                op3 = int(input("Por favor elige una opción: "))
                if op3 == 1:
                    print("Usted ha elegido la opción 1")
                    lb.ingresar_observaciones()
                    break
                elif op3 == 2:
                    print("Usted ha elegido la opción 2")
                    lb.consultar_observaciones()
                    break
                elif op3 == 3:
                    print("Usted ha elegido la opción 3")
                    break
        elif op == 4:
            print("Gracias por usar el programa.")
            break
else:
    print("Gracias por confiar en nosotros, vuelva pronto.")

