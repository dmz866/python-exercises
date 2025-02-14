#def suma(num1, num2, *args, **kwargs):
def suma(**kwargs):
    for key, val in kwargs.items():
        print(f'Key: {key} Value: {val}')

suma(x= 1, y = 2, z = 'David')