def reducir_lista(lista):
    lista_numeros = []
    max = 0

    for el in lista:
        if lista_numeros.count(el) == 0:
            lista_numeros.append(el)

        if el > max:
            max = el

    maxIndex = lista_numeros.index(max)
    lista_numeros.pop(maxIndex)

    return lista_numeros

print(reducir_lista([1,2,15,20, 7,2]))