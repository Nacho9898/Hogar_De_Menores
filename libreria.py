import re
# Función para validar el formato del RUT
def validar_rut(rut):
    # Verificar si el RUT tiene puntos
    if '.' in rut:
        return False
    # Separar el RUT y el dígito verificador
    rut, verificador = rut.split('-')
    # Verificar que el RUT tenga el formato correcto
    if not rut.isdigit() or len(rut) < 7:
        return False
    # Calcular el dígito verificador esperado
    suma = sum(int(digito) * (2 + i % 6) for i, digito in enumerate(reversed(rut)))
    verificador_esperado = str((11 - suma % 11) % 11)
    if verificador_esperado == '10':
        verificador_esperado = 'K'
    # Comparar el dígito verificador ingresado con el esperado
    return verificador.upper() == verificador_esperado

# Función para validar la sala
def validar_sala(sala):
    # La sala debe tener una letra mayúscula de la A-Z seguida de 1 o 2 números del 0 al 5
    return re.match(r'^[A-Z][0-5]{1,2}$', sala) is not None

# Función para ingresar los datos de un menor
def ingresar_datos():
    datos = {}
    datos["Nombres"] = input("Ingrese los nombres del menor: ")
    datos["Apellidos"] = input("Ingrese los apellidos del menor: ")
    
    # Bucle para solicitar la fecha de nacimiento hasta que sea válida o se agoten los intentos
    intentos = 3
    while intentos > 0:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del menor (DDMMAAAA): ")
        # Validar la fecha de nacimiento
        if not re.match(r'^\d{8}$', fecha_nacimiento):
            print("La fecha de nacimiento debe tener 8 dígitos.")
            intentos -= 1
            if intentos == 0:
                print("Se acabaron los intentos.")
                return None
            print(f"Intentos restantes: {intentos}")
        else:
            datos["Fecha de nacimiento (DD/MM/AAAA)"] = fecha_nacimiento
            break
    
    # Validar y solicitar la sala hasta que sea válida
    while True:
        sala = input("Ingrese la sala a la que pertenece el menor (con una letra mayúscula y 1 o 2 números del 0 al 5): ")
        if validar_sala(sala):
            datos["Sala a la que pertenece"] = sala
            break
        else:
            print("La sala ingresada no es válida. Por favor, inténtelo nuevamente.")

    # Bucle para solicitar el RUT hasta que sea válido o se agoten los intentos
    intentos = 3
    while intentos > 0:
        rut = input("Ingrese el RUT del menor (sin puntos, con guión y dígito verificador): ")
        if validar_rut(rut):
            datos["Rut"] = rut
            break  # Salir del bucle si el RUT es válido
        else:
            print("El Rut ingresado no es válido o contiene puntos.")
            intentos -= 1
            if intentos == 0:
                print("Se acabaron los intentos.")
                return None
    
    datos["Nacionalidad"] = input("Ingrese la nacionalidad del menor: ")
    return datos

# Función para consultar los datos de un menor
def consultar_datos(datos):
    if datos:
        print("Datos del menor:")
        for key, value in datos.items():
            if key == "Fecha de nacimiento (DDMMAAAA)":
                # Formatear la fecha de nacimiento al formato DD/MM/AAAA
                fecha_formateada = f"{value[:2]}-{value[2:4]}-{value[4:]}"
                print(f"{key}: {fecha_formateada}")
            else:
                print(f"{key}: {value}")
    else:
        print("No se encontraron datos para este menor.")

# Primera parte del programa para inicio de sesión con usuario y contraseña
def iniciar_sesion():
    intentos = 3
    while intentos > 0:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        # Validación de la contraseña
        # La contraseña debe tener al menos 9 caracteres
        if len(contraseña) < 9:
            print("La contraseña debe tener al menos 9 caracteres.")
        # La contraseña debe tener exactamente 1 mayúscula
        elif not any(char.isupper() for char in contraseña):
            print("La contraseña debe tener al menos una letra mayúscula.")
        # La contraseña debe tener exactamente 4 letras minúsculas
        elif sum(1 for char in contraseña if char.islower()) != 4:
            print("La contraseña debe tener exactamente 4 letras minúsculas.")
        # La contraseña debe tener exactamente 4 dígitos
        elif sum(1 for char in contraseña if char.isdigit()) != 4:
            print("La contraseña debe tener exactamente 4 dígitos.")
        # La contraseña debe ser igual al usuario
        elif contraseña != usuario:
            print("La contraseña debe ser igual al nombre de usuario.")
        else:
            print("¡Bienvenido!")
            return True  # Devuelve True si la autenticación es exitosa

        intentos -= 1
        if intentos > 0:
            print(f"Intentos restantes: {intentos}")
        else:
            print("Ha excedido el número de intentos. El programa se cerrará.")
            return False  # Devuelve False si se exceden los intentos


# Ciclo principal del programa
datos_del_menor = None  # Inicializamos los datos del menor como None

