# 17. Verifica si una persona tiene acceso VIP o normal en un evento.

tipo_entrada = input("¿Tienes entrada VIP? (sí/no): ").lower()
if tipo_entrada == "sí":
    print("Tienes acceso VIP.")
else:
    print("Tienes acceso normal.")