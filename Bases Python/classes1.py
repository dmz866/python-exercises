class Bird:
    has_wings = True

    def __init__(self, color): # self represents the instance
        self.color = color

    # Instance function
    # Change instance values
    # Change class values
    # Call other functions
    def fly(self, meters):
        self.scream()
        print(f'The bird flew {meters} meters')

    def scream(self):
        print(f'Pio {self.color}')

    # Can be called without an instance
    # Cannot access to instance attributes
    # Can access to class attributes
    @classmethod
    def lay_eggs(cls, quantity):
        print(f'Lay {quantity} eggs and has wings {cls.has_wings}')

    # Can be called without an instance
    # Cannot access class/instance attributes
    @staticmethod
    def watch():
        print('The bird watches the moon')

bird1 = Bird('blue')
bird1.fly(10)
bird1.has_wings = False

Bird.lay_eggs(20)
Bird.watch()