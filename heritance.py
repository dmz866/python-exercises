class Animal:
    def __init__(self, years, color):
        self.years = years
        self.color = color

    def born(self):
        print('It has borned')

class Bird(Animal):
    pass


# check parent classes
print(Bird.__bases__)

# check sub classes
print(Animal.__subclasses__())

bird1 = Bird(2, 'yellow')

bird1.born()
