# 13. Verifica si un número es múltiplo de 3 y 5.

num = int(input("Ingresa un número: "))
if num % 3 == 0 and num % 5 == 0:
    print("El número es múltiplo de 3 y 5.")
else:
    print("El número no es múltiplo de 3 y 5.")
