# ingresos = input("Cuantos ingresos has generado? ")
# #First Method
# print("Tu comision es de " + str(round(float(ingresos)*13/100, 2)))
# #Second Method
# print(f"Tu comision es de {round(float(ingresos)*13/100, 3)}")
# #Third Method
# print("Tu comision es de {}".format(round(float(ingresos)*13/100, 4)))

def max_custom(n1: int, n2: int):
    """
    This function checks which value is the highest and it returns it too.
    :param n1: int value
    :param n2: int value
    :return: the highest value
    """
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        raise Exception("Los valores son iguales")
    raise Exception("Algo salió mal")

print(max_custom(1,3))
print(max_custom(4,5))
print(max_custom('s', 323))