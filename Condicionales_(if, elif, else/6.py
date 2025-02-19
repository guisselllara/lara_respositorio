# 6. Verifica si un usuario ha ingresado la contraseña correcta.

password_correcta = "secreto123"
password_ingresada = input("Ingresa la contraseña: ")
if password_ingresada == password_correcta:
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta.")
