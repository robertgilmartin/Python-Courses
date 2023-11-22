# Try -- > Intenta ejecutar este código
# Except  --> En caso de que no puedas ejecutarlo haz esto.
# Finally --> Pase lo que pase, al final del proceso, ejecuta esto otro.

def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: ")) # --> Si inputeas una letra, por ejemplo, el error es ValueError
    print(n1 + n2)
    print("Gracias por sumar")
    print("Gracias por sumar" + n1) # --> TypeError

# En General hay muchos tipos de errores y para decir que excepciones debes tomar para cualquier tipo de error
# debes especificarlo en el except poniendo ese tipo de error.


try:
    # Codigo que queremos probar
    suma()
except TypeError:
    # Except para TypeError
    print("Estas intentando concatenar tipos distintos.")
except ValueError:
    # Except para ValueError
    print("Ese no es un numero")
else:
    # Codigo a ejecutar SI NO hay un error
    print("Hiciste todo bien")
finally:
    # Codigo que se va a ejecutar de todos modos
    print("Eso fue todo!")


def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")


pedir_numero()
