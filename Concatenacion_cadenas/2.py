# Concatena tres cadenas en una sola variable
import random
import string

def generar_cadena():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

cadena1 = generar_cadena()
cadena2 = generar_cadena()
cadena3 = generar_cadena()

resultado = cadena1 + " " + cadena2 + " " + cadena3

print("Tres cadenas:", resultado)

print("Tres cadenas:", cadena1 + " " + cadena2 + " " + cadena3)
