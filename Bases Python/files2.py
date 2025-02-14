import os
'''
route = os.getcwd() #current working directory
print(route)

route = os.chdir("C:\\Users\\dmz86\\OneDrive\\Desktop") #change directory
file1 = open('test33.txt')

os.makedirs("C:\\Users\\dmz86\\OneDrive\\Desktop\\TestFolder") #Create new directory

print(file1.read())
file1.close()
'''

routeFile = "C:\\Users\\dmz86\\OneDrive\\Desktop\\test33.txt"

directoryName = os.path.dirname(routeFile)
fileName = os.path.basename(routeFile)

file = os.path.split(routeFile) # Tuple file name and directory

#print(fileName, directoryName)
print(file)

#Delete directory
os.rmdir("C:\\Users\\dmz86\\OneDrive\\Desktop\\TestFolder")


