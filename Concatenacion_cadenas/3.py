# Une una cadena y un número convirtiéndolo a string
import random
import string

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
cadena1 = random_string

num6 = 42
print("Concatenar cadena y número:", cadena1 + " " + str(num6))
