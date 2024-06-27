def lista_del_personal1():
    personal = []  # Lista para almacenar datos del personal

    while True:
        print("Ingrese si quiere ver o agregar los datos del personal")
        print("1) Ver datos del personal")
        print("2) Agregar datos")
        print("3) Volver")
        res = int(input("Ingrese una opción: "))

        if res == 1:
            if not personal:
                print("No hay datos del personal ingresados.")
            else:
                print("Datos del personal:")
                for datos_persona in personal:
                    print("Datos de la persona:")
                    for key, value in datos_persona.items():
                        print(f"{key}: {value}")
                    print()  # Espacio entre datos de diferentes personas
                input("Presione cualquier tecla para volver al menú principal.")
        
        elif res == 2:
            datos_persona = {}  # Diccionario para almacenar los datos de una persona
            
            while True:
                nom1 = input("Ingrese el primer nombre: ")
                if nom1:
                    datos_persona["Primer Nombre"] = nom1
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while True:
                nom2 = input("Ingrese el segundo nombre: ")
                if nom2:
                    datos_persona["Segundo Nombre"] = nom2
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while True:
                ape1 = input("Ingrese el primer apellido: ")
                if ape1:
                    datos_persona["Primer Apellido"] = ape1
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while True:
                ape2 = input("Ingrese el segundo apellido: ")
                if ape2:
                    datos_persona["Segundo Apellido"] = ape2
                    break
                else:
                    print("No se puede dejar en blanco")
            
            def generar_rut_con_dv(rut_bas, dv):
                return f"{rut_bas}-{dv.upper()}"
            
            while True:
                rut_bas = input("Por favor ingrese su rut sin dígito de verificación y sin puntos: ")
                dv = input("Por favor ingrese el código de verificación: ")
                if rut_bas and dv:
                    rut_completo = generar_rut_con_dv(rut_bas, dv)
                    datos_persona["RUT"] = rut_completo
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while True:
                nac = input("Ingrese su Nacionalidad: ")
                if nac:
                    datos_persona["Nacionalidad"] = nac
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while True:
                vol_o_act = input("Ingrese si es voluntario o personal activo: ")
                if vol_o_act:
                    datos_persona["Tipo de Personal"] = vol_o_act
                    break
                else:
                    print("No se puede dejar en blanco")
            
            # Agregar los datos de la persona a la lista personal
            personal.append(datos_persona)
            print("Datos del personal ingresados correctamente.")
        
        elif res == 3:
            break



"""****************************************************************************************************************
opcion 1      """

def menu_principal():
    listamenor=[]
    while (True):
        print("======= Menú Principal =======")
        print("1) Ingresar datos del menor ")
        print("2) Consultar datos del menor")
        print("3) Salir                    ")
        respuesta = int(input("Ingrese el número de la opción que desea: "))
        if respuesta<1 or respuesta>3:
            print("opcion invalida")

        elif respuesta==1:
            while (True):
                print("Escriba el primer nombre del menor")
                nom1=input()
                if nom1:
                    listamenor.append(nom1)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while (True):
                print("Escriba el segundo nombre del menor")
                nom2=input()
                if nom2:
                    listamenor.append(nom2)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while (True):
                print("Ingrese la fecha de nacimiento del menor (Formato DD/MM/AAAA)")
                año=input()
                if año:
                    listamenor.append(año)
                    break
                else:
                    print ("No se puede dejar en blanco")
            
            while (True):
                print("Ingrese la sala a la que pertenece ( Debe tener 1 letra mayúscula,2 números del 0-5 )")
                sala=input()
                if sala:
                    listamenor.append(sala)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            def generar_rut_con_dv(rut_bas, dv):
                return f"{rut_bas}-{dv.upper()}"
            
            while (True):

                print("Porfavor ingrese su rut sin digito de verificacion y sin puntos")
                rut_bas=input()
                print("Porfavor ingrese el codigo de verificaciòn")
                dv=input()
                if rut_bas and dv:
                    rut_completo = generar_rut_con_dv(rut_bas, dv)
                    listamenor.append(rut_completo)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while (True):
                print("Ingrese la nacionalidad del menor")
                nacionalidad=input()
                if nacionalidad:
                    listamenor.append(nacionalidad)
                    break
                else:
                    print("No se puede dejar en blanco")
       
        elif respuesta==2:
            print(listamenor)
            print("Si desea volver al menu precione cualquier tecla")
            res90=input()
        
        elif respuesta==3:
            break




    