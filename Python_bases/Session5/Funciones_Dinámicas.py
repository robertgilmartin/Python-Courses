def check_3_cifras(numero):
     return numero in range(100, 1000)

suma = 586 + 402

resultado = check_3_cifras(suma)
print(resultado)


def check_3_cifrass(lista):
    for n in lista:
        if n in range(100, 1000):
           return True
        else:
            pass
    return False

resultado2 = check_3_cifrass([55,99,6000])
print(resultado2)


def check_3_cifrasss(lista):
    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado3 = check_3_cifrasss([55,992,600])
print(resultado3)
