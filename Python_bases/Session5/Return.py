def multiplicar(num1, num2):
    """
    Devuelve el producto entre dos valores
    :param num1: int
    :param num2: int
    :return: num1 * num2
    """
    result = num1 * num2
    return result

producto = multiplicar(1,6)

print(producto)

def invertir_palabra(palabra):
    lista = list(palabra)
    lista.reverse()
    return "".join(lista).upper()

print(invertir_palabra("Python"))
