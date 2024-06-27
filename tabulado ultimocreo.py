
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