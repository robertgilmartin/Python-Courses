# Key Word Args
# Es similar a la *args, pero se le puede dar un nombre a cada valor y se funciona como un diccionario.

def suma(**kwargs):
    total = 0

    print(type(kwargs))
    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")
        total += valor
    return total

print(suma(x=3, y=5, z=2))



# El orden es importante
def suma_con_args_y_kwargs(num1, num2, *args, **kwargs):
    print(f"el primer numero es el {num1}")
    print(f"el segundo numero es el {num2}")

    for arg in args:
        print(f"arg = {arg}")
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

suma_con_args_y_kwargs(15, 50, 400, 600,1200, x= 4, y= 12, r= 56)

args = [100, 200, 300, 500]
kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}

# Hay que poner los astericos
suma_con_args_y_kwargs(15,20,  *args, **kwargs)

def cantidad_atributos(**kwargs):
    return len(kwargs.values())