from random import shuffle

num = 1

match num:
    case 1:
        print('Uno')
    case 2:
        print("Dosh")
    case _:
        print('Error')



def lanzar_dados():
    valores = list(range(1, 7))
    shuffle(valores)
    return (valores[0], valores[1])


def evaluar_jugada(n1, n2):
    suma_dados = n1 + n2

    if(suma_dados <= 6):
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif (6 < suma_dados < 10):
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


n1, n2 = lanzar_dados()
print(evaluar_jugada(n1, n2))


