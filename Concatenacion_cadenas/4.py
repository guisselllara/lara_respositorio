# Concatena una cadena y una variable usando f-strings
import random
import string


def generar_cadena():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

cadena1 = generar_cadena()
cadena2 = generar_cadena()

print(f"F-string: {cadena1} {cadena2}")

