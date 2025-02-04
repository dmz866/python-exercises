def ordenar(pal):
    lista = []

    for el in pal:
        if el not in lista:
            lista.append(el)

    lista.sort()

    return lista


print(ordenar('entretenido'))