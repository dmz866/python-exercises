class Animal:
    def __init__(self, years, color):
        self.years = years
        self.color = color

    @staticmethod
    def born():
        print('Animal has borned')

class Bird(Animal):
    def __init__(self, years, color, name):
        super().__init__(years, color)
        self.name = name

    def born(self):
        super().born()
        print('Bird has borned')



# check parent classes
print(Bird.__bases__)

# check subclasses
print(Animal.__subclasses__())

bird1 = Bird(2, 'yellow', 'Dosh')

bird1.born()
