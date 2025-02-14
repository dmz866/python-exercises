class CD:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    #override str
    def __str__(self):
        return f'{self.name} - {self.title}'

    def __len__(self):
        return 10

    #deletes CD and prints string
    def __del__(self):
        print('CD eliminado')

cd1 = CD('LP', 'Faint')
#both return the same
print(cd1)
print(str(cd1))
print(len(cd1))

del cd1

#will fail since cd1 does not exist at this point
#print(cd1)