class Bird:
    has_wings = True

    def __init__(self, color): # self represents the instance
        self.color = color

    @staticmethod
    def fly(meters):
        print(f'The bird flew {meters} meters')

bird1 = Bird('blue')
bird2 = Bird('red')

bird1.fly(10)

print(bird1.color)
print(Bird.has_wings)
print(bird2.has_wings)


class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa('blanco', 4)