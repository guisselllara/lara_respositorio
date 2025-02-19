# 20. Compara tres números y determina el mayor.

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))
if a > b and a > c:
    print("El primer número es el mayor.")
elif b > c:
    print("El segundo número es el mayor.")
else:
    print("El tercer número es el mayor.")