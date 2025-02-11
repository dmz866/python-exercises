from pathlib import Path
from os import system

base = Path.home()
route1 = Path('Folder1', 'Subfolder2', 'testFile.txt')
route2 = route1.with_name('testFile2.txt')

print(base)
print(route1)
print(route2)
print(route2.stem) #route without extension
print(route1.parent)


my_route = Path('C:\\Users\\dmz86\\Documents\\DmZ\\Documentos')


#for e in my_route.glob('*.txt'): #Print All text files inside a directory
for e in my_route.glob('**/*.txt'): #Print All text files inside a directory and subdirectories
    print(e.name)

system('cls')


