global usuario
global contraseña
global intentos
menores = []
anotaciones_menores = []

def login():
    intentos = 0
    while intentos < 3:
        print("""
    Ingrese su usuario, recordar que los requisitos son:
    (1 Mayuscula, 4 Minusculas, 4 Números)
    tanto el usuario como la contraseña deben ser iguales. 

    EJ: Josef1234
    """)
        usuario = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese Contraseña: ")
        if usuario == contraseña and len(usuario) == 9 and \
        usuario[0].isupper() and usuario[1:5].islower() and usuario[5:].isdigit():
            print("Bienvenido")
            return True
        else:
            intentos += 1
            print(f"Inicio de sesión incorrecto. Te quedan {3 - intentos} intentos")
            if intentos == 3:
                print("Se ha bloqueado su cuenta. Inténtelo más tarde")
                return False

def ingresar_datos():
    menor = {}
    
    menor["Nombres"] = input("Ingrese los nombres del menor: ")
    menor["Apellidos"] = input("Ingrese los apellidos del menor: ")
    
    while True:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
        try:
            dia, mes, año = map(int, fecha_nacimiento.split('/'))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= año <= 2024:
                menor['Fecha de Nacimiento'] = fecha_nacimiento
                break
            else:
                print("Fecha no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Formato de fecha no válido. Inténtelo de nuevo.")
    
    while True:
        sala = input("Ingrese la sala a la que pertenece (formato: 1 letra mayúscula, 2 números del 0-5): ")
        if len(sala) == 3 and sala[0].isupper() and sala[1:].isdigit() and 0 <= int(sala[1]) <= 5 and 0 <= int(sala[2]) <= 5:
            menor['Sala'] = sala
            break
        else:
            print("Formato de sala no válido. Inténtelo de nuevo.")
    
    while True:
        rut = input("Ingrese el RUT (sin puntos, con guion verificador): ")
        if '-' in rut and len(rut.split('-')[0]) > 0 and len(rut.split('-')[1]) == 1:
            menor['RUT'] = rut
            break
        else:
            print("Formato de RUT no válido. Inténtelo de nuevo.")
    
    menor['Nacionalidad'] = input("Ingrese la nacionalidad del menor: ")

    # Agregar el menor a la lista
    menores.append(menor)
    print("Datos del menor ingresados correctamente.")

def consultar_datos():
    if menores:
        rut_consulta = input("Ingrese el RUT del menor que desea consultar (sin puntos, con guion verificador): ")
        menor = next((m for m in menores if m['RUT'] == rut_consulta), None)
        if menor:
            print("\nDatos del menor:")
            for key, value in menor.items():
                print(f"{key}: {value}")
        else:
            print("El RUT ingresado no coincide con los datos ingresados anteriormente.")
    else:
        print("No se han ingresado datos de ningún menor.")

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

def ingresar_observaciones():
    if menores:
        rut_consulta = input("Ingrese el RUT del menor para agregar una anotación (sin puntos, con guion verificador): ")
        menor = next((m for m in menores if m['RUT'] == rut_consulta), None)
        if menor:
            anotacion = input("Ingrese la anotación para el menor: ")
            anotaciones_menores.append({'menor': menor, 'anotaciones': [anotacion]})
            print("Anotación ingresada correctamente.")
        else:
            print("El RUT ingresado no coincide con los datos ingresados anteriormente.")
    else:
        print("No se han ingresado datos de ningún menor.")

def consultar_observaciones():
    if anotaciones_menores:
        rut_consulta = input("Ingrese el RUT del menor para consultar anotaciones (sin puntos, con guion verificador): ")
        menor = next((m for m in anotaciones_menores if m['menor']['RUT'] == rut_consulta), None)
        if menor:
            print("\nAnotaciones del menor:")
            for anotacion in menor['anotaciones']:
                print(f"- {anotacion}")
        else:
            print("El RUT ingresado no coincide con los datos ingresados anteriormente.")
    else:
        print("No se han ingresado datos de ningún menor.")