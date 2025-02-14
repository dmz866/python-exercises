#Generator functions allow you to declare a function that behaves like an iterator

def mi_generator(n):
    for el in range(1, n):
        yield el

def mi_generator2():
    a = 1
    yield a

    a += 1
    yield a

    a += 1
    yield a


n = 10
g = mi_generator(n)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('################################')

r = mi_generator2()
print(next(r))
print(next(r))
print(next(r))


def inf():
    n = 1

    while True:
        n += 1
        yield n


generador = inf()

print('################################')

print(next(generador))
print(next(generador))


def func():
    n = 0
    while True:
        n += 7
        yield n



f = func()

print('################################')

print(next(f))
print(next(f))
