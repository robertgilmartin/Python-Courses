def contar_primos(num):
    numeros = list(range(0, num))
    for n in numeros:
        if n%2 == 0:
            numeros.remove(n)
        else:
            pass
    numeros.remove(1)
    print(numeros)

contar_primos(20)