# 1. Verifica si un número es positivo o negativo.

num = int(input("Ingresa un número: "))
if num > 0:
    print("El número es negativo.")
elif num < 0:
    print("El número es positivo.")
else:
    print("El número es cero.")