from random import shuffle

def lanzar_moneda():
    res = ['Cara', 'Cruz']
    shuffle(res)

    return res[0]

def probar_suerte(res, lista):
    if res == 'Cara':
        print("La lista se autodestruirá")
        return []

    print("La lista fue salvada")
    return lista

print(probar_suerte(lanzar_moneda(), [1,2,3]))