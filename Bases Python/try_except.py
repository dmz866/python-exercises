def suma(n1, n2):
    try:
         res = n1 + n2
         print(f'{n1} + {n2} = {res}')
    except TypeError:
         print('Tipo de datos incorrecto')
    except ValueError:
        print('Ese no es nu numero!')
    else:
        print('Suma correcta!')
    finally:
        print('Finally')

suma(1, '4')
suma(1, 4)
