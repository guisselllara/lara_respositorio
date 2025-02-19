# 14. Crea un sistema de login con usuario y contraseña.

usuario_correcto = "admin"
password_correcta = "1234"
usuario = input("Usuario: ")
password = input("Contraseña: ")
if usuario == usuario_correcto and password == password_correcta:
    print("Inicio de sesión exitoso.")
else:
    print("Usuario o contraseña incorrectos.")
