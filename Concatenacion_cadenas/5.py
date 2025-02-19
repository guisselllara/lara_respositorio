# Une dos cadenas con el método join()

import random
import string

def generar_cadena():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


cadena1 = generar_cadena()
cadena2 = generar_cadena()
cadena3 = generar_cadena()

print("Join:", " - ".join([cadena1, cadena2, cadena3]))


