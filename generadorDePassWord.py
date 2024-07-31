import string
import random
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena

longitud = int(input("Ingrese la longitud de su contraseña:"))

nueva_contrasena = generar_contrasena(longitud)
print("la nueva clave es:", nueva_contrasena)