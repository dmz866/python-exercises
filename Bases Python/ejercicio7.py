from random import choice

palabras = ['casa', 'perro', 'trabajo']

def jugar():
    jugando = True
    palabra = choice(palabras)
    palabra_oculta = list('*' * len(palabra))
    total_intentos = len(palabra)
    intentos = 0
    letra_es_valida = False

    while jugando:
        print(''.join(palabra_oculta))
        letra = ''
        letra_es_valida = False

        while not letra_es_valida:
            letra = input('Elija una letra: ').lower()

            if len(letra) == 1 and letra.isalpha():
                letra_es_valida = True

        if intentos == total_intentos:
            jugando = False
            print("Perdiste")
            break

        total_indx = []

        for idx, e in enumerate(palabra):
            if e == letra:
                palabra_oculta[idx] = letra

        intentos = intentos + 1

        if palabra_oculta.count('*') == 0:
            print("Ganaste!")
jugar()


