#decorators modify the behaviour of functions
def salute_decorator(func):
    def say_hi(word):
        print('Hi')
        func(word)
        print('Bye')

    return say_hi


@salute_decorator
def to_uppercase(t):
    print(t.upper())


to_uppercase('dosh')




