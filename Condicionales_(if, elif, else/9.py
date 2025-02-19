# 9. Usa elif para clasificar un número en rango bajo, medio o alto.

num = int(input("Ingresa un número: "))
if num < 10:
    print("Número bajo.")
elif 10 <= num <= 50:
    print("Número medio.")
else:
    print("Número alto.")