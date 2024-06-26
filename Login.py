
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