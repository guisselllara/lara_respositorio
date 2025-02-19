# 19. Evalúa si una letra ingresada es vocal o consonante.

letra = input("Ingresa una letra: ").lower()
if letra in "aeiou":
    print("Es una vocal.")
else:
    print("Es una consonante.")