def ordenar_letras_de_una_palabra(palabra):
    mi_set = set(palabra)
    lista = list(mi_set)
    lista.sort()
    return lista

print(ordenar_letras_de_una_palabra('entretenido'))