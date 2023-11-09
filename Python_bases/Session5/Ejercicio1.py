def valor_intermedio(num1, num2, num3):
    if num2 < num1 < num3 or num3 < num1 < num2:
        return num1
    elif num1 < num2 < num3 or num3 < num2 < num1:
        return num2
    else:
        return num3

def devolver_distinto(num1, num2, num3):
    """
    Devuelve el valor mayor, menor o intermedio segÚn el resultado de la suma
    :param num1: int
    :param num2: int
    :param num3: int
    :return: mayor, menor o intermedio
    """
    suma = num1 + num2 + num3
    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    intermedio = valor_intermedio(num1, num2, num3)

    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else:
        return intermedio

print(devolver_distinto(6,5,4))