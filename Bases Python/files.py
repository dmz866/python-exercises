'''

file1 = open('test.txt')
print(file1.read())
file1.close()

file1 = open('test.txt')
print(file1.readline())
print(file1.readline())
file1.close()


file1 = open('test.txt')

for l in file1:
    print(f'New Line: {l}')

file1.close()

# An item for each line
file1 = open('test.txt')
allLinesList = file1.readlines()
print(allLinesList)


#Overwrites the content of the file
file1 = open('test.txt', 'w')
file1.write('test 1\n')
file1.close()


#Appends text to the content of the file
file1 = open('test.txt', 'a')
file1.write('test 2')
file1.close()
'''




