class Father:
    def laugh(self):
        print('Father laugh')


class Mother:
    def laugh(self):
        print('Mother laugh')

class Son(Father, Mother):
    pass


son1 = Son()
son1.laugh()

# classes that are considered when looking for base classes during method resolution.
print(Son.__mro__)