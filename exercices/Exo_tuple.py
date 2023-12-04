def operations(nombre1, nombre2):
    return nombre1 + nombre2, nombre1 - nombre2, nombre1 / nombre2, nombre1 * nombre2

nombre1 = float(input("nombre 1 : "))
nombre2 = float(input("nombre 2 : "))


add, sub, div, mul = operations(nombre1, nombre2)

print("l'addition = ", add)
print("soustraction = ", sub)
print("division = ", div)
print("multiplication = ", mul)

